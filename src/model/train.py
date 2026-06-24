import os
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import ImageFolder
from torch.optim import AdamW
from torch.optim.lr_scheduler import CosineAnnealingLR
from tqdm import tqdm
from pathlib import Path
import json

from src.model.efficientnet import (
    PlantDiseaseModel,
    freeze_backbone,
    unfreeze_backbone,
    save_model,
    get_device,
    count_parameters,
)
from src.utils.preprocessing import get_train_transforms, get_val_transforms


# ── Config ──────────────────────────────────────────────────
class TrainConfig:
    DATA_DIR      = "data/raw"
    SAVE_DIR      = "models"
    NUM_CLASSES   = 38
    IMAGE_SIZE    = 300
    BATCH_SIZE    = 32
    NUM_WORKERS   = 4
    PIN_MEMORY    = True

    # Phase 1 — head only
    PHASE1_EPOCHS = 5
    PHASE1_LR     = 1e-3

    # Phase 2 — full fine-tune
    PHASE2_EPOCHS = 15
    PHASE2_LR     = 1e-4

    VAL_SPLIT     = 0.15
    SEED          = 42


# ── Dataset ─────────────────────────────────────────────────
def build_dataloaders(cfg: TrainConfig):
    """Build train/val dataloaders from ImageFolder structure."""

    full_dataset = ImageFolder(
        root=cfg.DATA_DIR,
        transform=get_train_transforms(),
    )

    # Save class names
    class_names = full_dataset.classes
    Path(cfg.SAVE_DIR).mkdir(parents=True, exist_ok=True)
    with open(f"{cfg.SAVE_DIR}/class_names.json", "w") as f:
        json.dump(class_names, f, indent=2)
    print(f"Classes found: {len(class_names)}")

    # Split train / val
    val_size   = int(len(full_dataset) * cfg.VAL_SPLIT)
    train_size = len(full_dataset) - val_size
    generator  = torch.Generator().manual_seed(cfg.SEED)

    train_dataset, val_dataset = random_split(
        full_dataset, [train_size, val_size], generator=generator
    )

    # Val dataset uses clean transforms (no augmentation)
    val_dataset.dataset.transform = get_val_transforms()

    train_loader = DataLoader(
        train_dataset,
        batch_size=cfg.BATCH_SIZE,
        shuffle=True,
        num_workers=cfg.NUM_WORKERS,
        pin_memory=cfg.PIN_MEMORY,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=cfg.BATCH_SIZE,
        shuffle=False,
        num_workers=cfg.NUM_WORKERS,
        pin_memory=cfg.PIN_MEMORY,
    )

    return train_loader, val_loader, class_names


# ── Train One Epoch ─────────────────────────────────────────
def train_epoch(model, loader, criterion, optimizer, device) -> dict:
    model.train()
    total_loss, correct, total = 0.0, 0, 0

    for images, labels in tqdm(loader, desc="Training", leave=False):
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss    = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item() * images.size(0)
        correct    += (outputs.argmax(1) == labels).sum().item()
        total      += images.size(0)

    return {
        "loss"    : total_loss / total,
        "accuracy": correct / total,
    }


# ── Validate ─────────────────────────────────────────────────
@torch.no_grad()
def validate_epoch(model, loader, criterion, device) -> dict:
    model.eval()
    total_loss, correct, total = 0.0, 0, 0

    for images, labels in tqdm(loader, desc="Validating", leave=False):
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        loss    = criterion(outputs, labels)

        total_loss += loss.item() * images.size(0)
        correct    += (outputs.argmax(1) == labels).sum().item()
        total      += images.size(0)

    return {
        "loss"    : total_loss / total,
        "accuracy": correct / total,
    }


# ── Main Training Loop ───────────────────────────────────────
def train(cfg: TrainConfig = TrainConfig()):
    device = get_device()

    # Build data
    train_loader, val_loader, class_names = build_dataloaders(cfg)

    # Build model
    model = PlantDiseaseModel(num_classes=len(class_names)).to(device)
    criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

    history = {"train_loss": [], "val_loss": [], "train_acc": [], "val_acc": []}
    best_val_acc = 0.0

    # ── Phase 1: Train head only ──────────────────────────────
    print("\n── Phase 1: Training classifier head ──")
    freeze_backbone(model)
    count_parameters(model)

    optimizer  = AdamW(filter(lambda p: p.requires_grad, model.parameters()), lr=cfg.PHASE1_LR)
    scheduler  = CosineAnnealingLR(optimizer, T_max=cfg.PHASE1_EPOCHS)

    for epoch in range(cfg.PHASE1_EPOCHS):
        train_metrics = train_epoch(model, train_loader, criterion, optimizer, device)
        val_metrics   = validate_epoch(model, val_loader, criterion, device)
        scheduler.step()

        _log_epoch(epoch + 1, cfg.PHASE1_EPOCHS, train_metrics, val_metrics)
        _update_history(history, train_metrics, val_metrics)

        if val_metrics["accuracy"] > best_val_acc:
            best_val_acc = val_metrics["accuracy"]
            save_model(model, f"{cfg.SAVE_DIR}/best_model.pt", {"phase": 1, "val_acc": best_val_acc})

    # ── Phase 2: Full fine-tune ───────────────────────────────
    print("\n── Phase 2: Full fine-tuning ──")
    unfreeze_backbone(model)
    count_parameters(model)

    optimizer = AdamW(model.parameters(), lr=cfg.PHASE2_LR, weight_decay=1e-4)
    scheduler = CosineAnnealingLR(optimizer, T_max=cfg.PHASE2_EPOCHS)

    for epoch in range(cfg.PHASE2_EPOCHS):
        train_metrics = train_epoch(model, train_loader, criterion, optimizer, device)
        val_metrics   = validate_epoch(model, val_loader, criterion, device)
        scheduler.step()

        _log_epoch(epoch + 1, cfg.PHASE2_EPOCHS, train_metrics, val_metrics)
        _update_history(history, train_metrics, val_metrics)

        if val_metrics["accuracy"] > best_val_acc:
            best_val_acc = val_metrics["accuracy"]
            save_model(model, f"{cfg.SAVE_DIR}/best_model.pt", {"phase": 2, "val_acc": best_val_acc})

    # Save history
    with open(f"{cfg.SAVE_DIR}/history.json", "w") as f:
        json.dump(history, f, indent=2)

    print(f"\nBest Val Accuracy: {best_val_acc:.4f}")
    return model, history


# ── Helpers ──────────────────────────────────────────────────
def _log_epoch(epoch, total, train, val):
    print(
        f"Epoch {epoch:02d}/{total} │ "
        f"Train Loss: {train['loss']:.4f} Acc: {train['accuracy']:.4f} │ "
        f"Val Loss: {val['loss']:.4f} Acc: {val['accuracy']:.4f}"
    )


def _update_history(history, train, val):
    history["train_loss"].append(train["loss"])
    history["val_loss"].append(val["loss"])
    history["train_acc"].append(train["accuracy"])
    history["val_acc"].append(val["accuracy"])


if __name__ == "__main__":
    train()