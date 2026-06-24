import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from io import BytesIO
from PIL import Image

from src.api.main import app
from src.api.schemas import PredictResponse, HealthResponse


# ── Test Client ───────────────────────────────────────────────
@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


# ── Mock Prediction ───────────────────────────────────────────
@pytest.fixture
def mock_prediction():
    return {
        "top_prediction": {
            "class_name" : "Tomato___Early_blight",
            "disease"    : "Early Blight",
            "plant"      : "Tomato",
            "confidence" : 0.92,
        },
        "all_predictions": [
            {"class_name": "Tomato___Early_blight", "disease": "Early Blight",  "plant": "Tomato", "confidence": 0.92},
            {"class_name": "Tomato___Late_blight",  "disease": "Late Blight",   "plant": "Tomato", "confidence": 0.06},
            {"class_name": "Tomato___Leaf_Mold",    "disease": "Leaf Mold",     "plant": "Tomato", "confidence": 0.02},
        ],
        "disease_info": {
            "name"          : "Early Blight",
            "name_ar"       : "اللفحة المبكرة",
            "plant"         : "Tomato",
            "severity"      : "medium",
            "severity_color": "#f97316",
            "description"   : "Fungal disease causing dark spots.",
            "treatments"    : ["Spray Chlorothalonil"],
            "prevention"    : ["Avoid overhead irrigation"],
        },
        "image_width"      : 300,
        "image_height"     : 300,
        "gradcam_image"    : None,
        "inference_time_ms": 120.5,
        "model_version"    : "efficientnet_b3_v1",
    }


# ── Helper: Create dummy image ────────────────────────────────
def create_test_image(format: str = "JPEG") -> BytesIO:
    """Create a simple green test image."""
    img    = Image.new("RGB", (300, 300), color=(34, 139, 34))
    buffer = BytesIO()
    img.save(buffer, format=format)
    buffer.seek(0)
    return buffer


# ── Health Check Tests ────────────────────────────────────────
class TestHealthEndpoint:

    def test_health_returns_200(self, client):
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_response_structure(self, client):
        response = client.get("/health")
        data     = response.json()
        assert "status"       in data
        assert "model_loaded" in data
        assert "num_classes"  in data
        assert "device"       in data

    def test_health_status_ok(self, client):
        response = client.get("/health")
        assert response.json()["status"] == "ok"


# ── Root Endpoint Tests ───────────────────────────────────────
class TestRootEndpoint:

    def test_root_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_root_has_docs_link(self, client):
        response = client.get("/")
        assert "docs" in response.json()


# ── Classes Endpoint Tests ────────────────────────────────────
class TestClassesEndpoint:

    def test_classes_returns_200(self, client):
        response = client.get("/classes")
        assert response.status_code == 200

    def test_classes_has_num_classes(self, client):
        response = client.get("/classes")
        data     = response.json()
        assert "num_classes" in data
        assert "classes"     in data
        assert isinstance(data["classes"], list)


# ── Predict Endpoint Tests ────────────────────────────────────
class TestPredictEndpoint:

    def test_predict_valid_image(self, client, mock_prediction):
        with patch("src.api.main.run_prediction", return_value=mock_prediction):
            image = create_test_image()
            response = client.post(
                "/predict",
                files={"file": ("test_leaf.jpg", image, "image/jpeg")},
            )
            assert response.status_code == 200

    def test_predict_returns_correct_fields(self, client, mock_prediction):
        with patch("src.api.main.run_prediction", return_value=mock_prediction):
            image    = create_test_image()
            response = client.post(
                "/predict",
                files={"file": ("test_leaf.jpg", image, "image/jpeg")},
            )
            data = response.json()
            assert "top_prediction"  in data
            assert "all_predictions" in data
            assert "disease_info"    in data

    def test_predict_no_file_returns_422(self, client):
        response = client.post("/predict")
        assert response.status_code == 422

    def test_predict_png_image(self, client, mock_prediction):
        with patch("src.api.main.run_prediction", return_value=mock_prediction):
            image    = create_test_image(format="PNG")
            response = client.post(
                "/predict",
                files={"file": ("test_leaf.png", image, "image/png")},
            )
            assert response.status_code == 200


# ── Preprocessing Tests ───────────────────────────────────────
class TestPreprocessing:

    def test_validate_image_valid_jpg(self):
        from src.utils.preprocessing import validate_image
        is_valid, msg = validate_image("leaf.jpg", 1024 * 1024)
        assert is_valid is True
        assert msg == ""

    def test_validate_image_invalid_extension(self):
        from src.utils.preprocessing import validate_image
        is_valid, msg = validate_image("leaf.gif", 1024)
        assert is_valid is False
        assert "Unsupported" in msg

    def test_validate_image_too_large(self):
        from src.utils.preprocessing import validate_image
        is_valid, msg = validate_image("leaf.jpg", 20 * 1024 * 1024)
        assert is_valid is False
        assert "large" in msg

    def test_preprocess_image_output_shape(self):
        from src.utils.preprocessing import preprocess_image
        image  = Image.new("RGB", (300, 300))
        tensor = preprocess_image(image)
        assert tensor.shape == (1, 3, 300, 300)


# ── Disease Info Tests ────────────────────────────────────────
class TestDiseaseInfo:

    def test_get_known_disease(self):
        from src.utils.disease_info import get_disease_info
        info = get_disease_info("Tomato___Early_blight")
        assert info.name     == "Early Blight"
        assert info.plant    == "Tomato"
        assert info.severity == "medium"

    def test_get_unknown_disease_returns_default(self):
        from src.utils.disease_info import get_disease_info
        info = get_disease_info("Unknown___Disease")
        assert info is not None
        assert len(info.treatments) > 0

    def test_severity_color_medium(self):
        from src.utils.disease_info import get_severity_color
        color = get_severity_color("medium")
        assert color == "#f97316"

    def test_severity_color_high(self):
        from src.utils.disease_info import get_severity_color
        color = get_severity_color("high")
        assert color == "#ef4444"