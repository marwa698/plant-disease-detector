# 🌿 Plant Disease Detector

> An end-to-end ML system that detects plant diseases from leaf images using EfficientNet-B3 with **92%+ accuracy** on 38 disease classes.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.1-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

| Property | Details |
|---|---|
| Dataset | PlantVillage (54,000 images) |
| Model | EfficientNet-B3 (fine-tuned) |
| Classes | 38 plant disease types |
| Accuracy | 97% on test set |
| Inference Time | ~120ms per image |

---

## 🏗️ Project Structure
plant-disease-detector/

├── data/               # Dataset (raw + processed)

├── notebooks/          # EDA, training, evaluation

├── src/

│   ├── model/          # EfficientNet + Grad-CAM

│   ├── api/            # FastAPI backend

│   └── utils/          # Preprocessing + disease info

├── models/             # Saved model weights

└── tests/              # Unit tests
---

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/YOUR_USERNAME/plant-disease-detector.git
cd plant-disease-detector
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

### 2. Run API
```bash
uvicorn src.api.main:app --reload
```

### 3. Test Endpoint
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "accept: application/json" \
  -F "file=@sample_leaf.jpg"
```

---

## 📊 Results

| Metric | Score |
|---|---|
| Test Accuracy | 97.2% |
| F1-Score (macro) | 0.971 |
| Inference Time | 120ms |

---

## 🛠️ Tech Stack

- **Model**: EfficientNet-B3, Transfer Learning, Grad-CAM
- **Backend**: FastAPI, Uvicorn
- **Training**: PyTorch, timm
- **Deployment**: Docker, GitHub Actions

---

## 👤 Author
** Marwa Yosry ** — [LinkedIn](https://linkedin.com/in/yourprofile) · [GitHub](https://github.com/marw)