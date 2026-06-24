# ── Variables ─────────────────────────────────────────────────
PYTHON     = venv\Scripts\python
PIP        = venv\Scripts\pip
UVICORN    = venv\Scripts\uvicorn
PYTEST     = venv\Scripts\pytest

# ── Help ──────────────────────────────────────────────────────
.PHONY: help
help:
	@echo.
	@echo  Plant Disease Detector - Available Commands
	@echo  ============================================
	@echo  make install      Install all dependencies
	@echo  make serve        Run API server
	@echo  make train        Train the model
	@echo  make test         Run all tests
	@echo  make docker-build Build Docker image
	@echo  make docker-run   Run with Docker
	@echo  make clean        Clean cache files
	@echo.

# ── Setup ─────────────────────────────────────────────────────
.PHONY: install
install:
	python -m venv venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo Dependencies installed successfully!

# ── Development ───────────────────────────────────────────────
.PHONY: serve
serve:
	$(UVICORN) src.api.main:app --host 0.0.0.0 --port 8000 --reload

.PHONY: serve-prod
serve-prod:
	$(UVICORN) src.api.main:app --host 0.0.0.0 --port 8000 --workers 2

# ── Training ──────────────────────────────────────────────────
.PHONY: train
train:
	$(PYTHON) -m src.model.train

# ── Testing ───────────────────────────────────────────────────
.PHONY: test
test:
	$(PYTEST) tests/ -v --tb=short

.PHONY: test-coverage
test-coverage:
	$(PYTEST) tests/ -v --cov=src --cov-report=term-missing

# ── Docker ────────────────────────────────────────────────────
.PHONY: docker-build
docker-build:
	docker build -t plant-disease-detector .

.PHONY: docker-run
docker-run:
	docker-compose up --build

.PHONY: docker-down
docker-down:
	docker-compose down

# ── Clean ─────────────────────────────────────────────────────
.PHONY: clean
clean:
	del /s /q __pycache__ 2>nul
	del /s /q *.pyc 2>nul
	del /s /q .pytest_cache 2>nul
	@echo Cleaned successfully!