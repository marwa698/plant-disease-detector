from dataclasses import dataclass
from typing import List

@dataclass
class DiseaseInfo:
    name: str
    name_ar: str
    plant: str
    severity: str  # "low", "medium", "high"
    description: str
    treatments: List[str]
    prevention: List[str]

DISEASE_DATABASE = {
    "Tomato___Early_blight": DiseaseInfo(
        name="Early Blight",
        name_ar="اللفحة المبكرة",
        plant="Tomato",
        severity="medium",
        description="Fungal disease causing dark spots with concentric rings on leaves.",
        treatments=[
            "Spray fungicide containing Chlorothalonil",
            "Remove and destroy infected leaves immediately",
            "Apply copper-based fungicide every 7 days",
        ],
        prevention=[
            "Avoid overhead irrigation",
            "Ensure proper plant spacing for airflow",
            "Rotate crops every season",
        ],
    ),
    "Tomato___Late_blight": DiseaseInfo(
        name="Late Blight",
        name_ar="اللفحة المتأخرة",
        plant="Tomato",
        severity="high",
        description="Severe fungal disease that can destroy entire crops rapidly.",
        treatments=[
            "Apply Mancozeb or Metalaxyl fungicide",
            "Remove infected plants to prevent spread",
            "Spray every 5 days during wet weather",
        ],
        prevention=[
            "Use resistant tomato varieties",
            "Avoid working in wet fields",
            "Destroy all plant debris after harvest",
        ],
    ),
    "Tomato___Leaf_Mold": DiseaseInfo(
        name="Leaf Mold",
        name_ar="عفن الأوراق",
        plant="Tomato",
        severity="medium",
        description="Fungal disease thriving in high humidity environments.",
        treatments=[
            "Improve greenhouse ventilation",
            "Apply fungicide with Mancozeb",
            "Reduce humidity below 85%",
        ],
        prevention=[
            "Plant in well-ventilated areas",
            "Avoid wetting foliage when watering",
            "Use disease-resistant varieties",
        ],
    ),
    "Tomato___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Tomato",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Continue regular watering schedule",
            "Monitor weekly for early signs",
            "Maintain proper nutrition",
        ],
    ),
    "Potato___Early_blight": DiseaseInfo(
        name="Early Blight",
        name_ar="اللفحة المبكرة",
        plant="Potato",
        severity="medium",
        description="Fungal disease causing dark lesions on older leaves first.",
        treatments=[
            "Apply Chlorothalonil or Mancozeb",
            "Remove infected lower leaves",
            "Repeat spray every 7-10 days",
        ],
        prevention=[
            "Use certified disease-free seed potatoes",
            "Avoid overhead irrigation",
            "Maintain adequate soil nutrients",
        ],
    ),
    "Potato___Late_blight": DiseaseInfo(
        name="Late Blight",
        name_ar="اللفحة المتأخرة",
        plant="Potato",
        severity="high",
        description="Highly destructive disease — caused the Irish Potato Famine.",
        treatments=[
            "Apply Metalaxyl-based fungicide immediately",
            "Destroy all infected plant material",
            "Do not store infected tubers",
        ],
        prevention=[
            "Plant resistant varieties",
            "Hill up soil around plants",
            "Avoid planting in previously infected fields",
        ],
    ),
    "Potato___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Potato",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Maintain regular inspection",
            "Ensure proper drainage",
            "Rotate crops annually",
        ],
    ),
    "Corn_(maize)___Common_rust_": DiseaseInfo(
        name="Common Rust",
        name_ar="الصدأ الشائع",
        plant="Corn",
        severity="medium",
        description="Fungal disease causing reddish-brown pustules on leaf surfaces.",
        treatments=[
            "Apply Propiconazole fungicide",
            "Spray at first sign of pustules",
            "Repeat after 14 days if needed",
        ],
        prevention=[
            "Plant rust-resistant hybrids",
            "Early planting to avoid peak infection periods",
            "Monitor fields regularly",
        ],
    ),
    "Corn_(maize)___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Corn",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Maintain balanced fertilization",
            "Ensure good drainage",
            "Scout fields weekly",
        ],
    ),
    "Apple___Cedar_apple_rust": DiseaseInfo(
        name="Cedar Apple Rust",
        name_ar="صدأ التفاح",
        plant="Apple",
        severity="medium",
        description="Fungal disease causing orange spots on apple leaves.",
        treatments=[
            "Apply Myclobutanil fungicide at bud break",
            "Remove nearby cedar/juniper trees if possible",
            "Spray every 7-10 days during wet weather",
        ],
        prevention=[
            "Plant rust-resistant apple varieties",
            "Avoid planting near cedar trees",
            "Monitor leaves weekly in spring",
        ],
    ),
    "Apple___Apple_scab": DiseaseInfo(
        name="Apple Scab",
        name_ar="جرب التفاح",
        plant="Apple",
        severity="medium",
        description="Fungal disease causing dark scabby lesions on leaves and fruit.",
        treatments=[
            "Apply Captan or Mancozeb fungicide",
            "Remove and destroy fallen infected leaves",
            "Spray every 7 days during rainy season",
        ],
        prevention=[
            "Plant scab-resistant varieties",
            "Ensure good air circulation",
            "Clean up fallen leaves in autumn",
        ],
    ),
    "Apple___Black_rot": DiseaseInfo(
        name="Black Rot",
        name_ar="العفن الأسود",
        plant="Apple",
        severity="high",
        description="Fungal disease causing black rotting lesions on fruit and leaves.",
        treatments=[
            "Apply Captan-based fungicide",
            "Prune and destroy infected branches",
            "Remove mummified fruits from tree",
        ],
        prevention=[
            "Maintain good orchard sanitation",
            "Prune dead wood regularly",
            "Avoid wounding trees during pruning",
        ],
    ),
    "Apple___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Apple",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Continue regular monitoring",
            "Maintain proper fertilization",
            "Ensure adequate irrigation",
        ],
    ),
    "Grape___Black_rot": DiseaseInfo(
        name="Black Rot",
        name_ar="العفن الأسود",
        plant="Grape",
        severity="high",
        description="Fungal disease causing black shriveled berries and leaf spots.",
        treatments=[
            "Apply Mancozeb or Myclobutanil",
            "Remove and destroy infected berries",
            "Spray every 10 days from bud break",
        ],
        prevention=[
            "Prune vines for good air circulation",
            "Remove mummified berries",
            "Avoid overhead irrigation",
        ],
    ),
    "Grape___Esca_(Black_Measles)": DiseaseInfo(
        name="Esca (Black Measles)",
        name_ar="مرض الإسكا",
        plant="Grape",
        severity="high",
        description="Fungal disease causing tiger-stripe patterns on leaves.",
        treatments=[
            "No chemical cure available",
            "Remove and burn infected wood",
            "Apply wound protectants after pruning",
        ],
        prevention=[
            "Use clean pruning tools",
            "Prune during dry weather",
            "Protect pruning wounds immediately",
        ],
    ),
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": DiseaseInfo(
        name="Leaf Blight",
        name_ar="لفحة العنب",
        plant="Grape",
        severity="medium",
        description="Fungal disease causing dark brown spots on grape leaves.",
        treatments=[
            "Apply copper-based fungicide",
            "Remove infected leaves immediately",
            "Spray Mancozeb every 14 days",
        ],
        prevention=[
            "Ensure good air circulation",
            "Avoid wetting foliage",
            "Monitor weekly during humid weather",
        ],
    ),
    "Grape___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Grape",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Maintain regular pruning schedule",
            "Monitor for early disease signs",
            "Ensure proper nutrition",
        ],
    ),
    "Pepper,_bell___Bacterial_spot": DiseaseInfo(
        name="Bacterial Spot",
        name_ar="التبقع البكتيري",
        plant="Pepper",
        severity="high",
        description="Bacterial disease causing water-soaked spots on leaves and fruit.",
        treatments=[
            "Apply copper bactericide immediately",
            "Remove heavily infected plants",
            "Avoid working in wet fields",
        ],
        prevention=[
            "Use certified disease-free seeds",
            "Rotate crops every 2-3 years",
            "Avoid overhead irrigation",
        ],
    ),
    "Pepper,_bell___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Pepper",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Maintain proper spacing",
            "Monitor weekly for disease signs",
            "Ensure adequate drainage",
        ],
    ),
    "Strawberry___Leaf_scorch": DiseaseInfo(
        name="Leaf Scorch",
        name_ar="احتراق أوراق الفراولة",
        plant="Strawberry",
        severity="medium",
        description="Fungal disease causing purple spots that merge into large scorched areas.",
        treatments=[
            "Apply Captan or Thiram fungicide",
            "Remove and destroy infected leaves",
            "Spray every 7-10 days",
        ],
        prevention=[
            "Plant resistant varieties",
            "Avoid overhead watering",
            "Ensure good air circulation between plants",
        ],
    ),
    "Strawberry___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Strawberry",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Maintain proper plant spacing",
            "Remove old leaves regularly",
            "Monitor for signs of disease weekly",
        ],
    ),
    "Peach___Bacterial_spot": DiseaseInfo(
        name="Bacterial Spot",
        name_ar="التبقع البكتيري",
        plant="Peach",
        severity="high",
        description="Bacterial disease causing water-soaked lesions on leaves and fruit.",
        treatments=[
            "Apply copper-based bactericide",
            "Remove infected fruit and leaves",
            "Spray during dormant season",
        ],
        prevention=[
            "Plant resistant peach varieties",
            "Avoid working in wet conditions",
            "Prune for good air circulation",
        ],
    ),
    "Peach___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Peach",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Regular pruning for air circulation",
            "Monitor for early disease signs",
            "Maintain proper fertilization",
        ],
    ),
    "Cherry_(including_sour)___Powdery_mildew": DiseaseInfo(
        name="Powdery Mildew",
        name_ar="البياض الدقيقي",
        plant="Cherry",
        severity="medium",
        description="Fungal disease causing white powdery coating on leaves.",
        treatments=[
            "Apply Sulfur or Potassium bicarbonate",
            "Remove heavily infected shoots",
            "Spray every 7-14 days",
        ],
        prevention=[
            "Plant in sunny well-ventilated areas",
            "Avoid excessive nitrogen fertilization",
            "Use resistant cherry varieties",
        ],
    ),
    "Cherry_(including_sour)___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Cherry",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Maintain good orchard hygiene",
            "Regular monitoring for disease",
            "Proper pruning for air flow",
        ],
    ),
    "Squash___Powdery_mildew": DiseaseInfo(
        name="Powdery Mildew",
        name_ar="البياض الدقيقي",
        plant="Squash",
        severity="medium",
        description="Fungal disease causing white powder on leaf surfaces.",
        treatments=[
            "Apply Neem oil or Sulfur spray",
            "Remove infected leaves",
            "Spray baking soda solution (1 tbsp per liter)",
        ],
        prevention=[
            "Plant in full sun locations",
            "Avoid overcrowding plants",
            "Water at base not on leaves",
        ],
    ),
    "Blueberry___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Blueberry",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Maintain acidic soil pH 4.5-5.5",
            "Monitor for disease weekly",
            "Ensure proper drainage",
        ],
    ),
    "Raspberry___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Raspberry",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Prune old canes after harvest",
            "Maintain good air circulation",
            "Monitor for pests and disease",
        ],
    ),
    "Soybean___healthy": DiseaseInfo(
        name="Healthy",
        name_ar="سليم",
        plant="Soybean",
        severity="low",
        description="Plant appears healthy with no signs of disease.",
        treatments=[],
        prevention=[
            "Rotate crops annually",
            "Use certified disease-free seeds",
            "Monitor fields regularly",
        ],
    ),
    "Orange___Haunglongbing_(Citrus_greening)": DiseaseInfo(
        name="Citrus Greening (HLB)",
        name_ar="اخضرار الحمضيات",
        plant="Orange",
        severity="high",
        description="Deadly bacterial disease spread by insects — no cure available.",
        treatments=[
            "Remove and destroy infected trees",
            "Control Asian citrus psyllid insect",
            "Apply systemic insecticides",
        ],
        prevention=[
            "Use certified disease-free nursery plants",
            "Monitor for psyllid insects",
            "Quarantine new plants before planting",
        ],
    ),
    "Corn_(maize)___Northern_Leaf_Blight": DiseaseInfo(
        name="Northern Leaf Blight",
        name_ar="لفحة الذرة الشمالية",
        plant="Corn",
        severity="high",
        description="Fungal disease causing long grey-green lesions on corn leaves.",
        treatments=[
            "Apply Propiconazole or Azoxystrobin",
            "Spray at first sign of lesions",
            "Repeat after 14 days if needed",
        ],
        prevention=[
            "Plant resistant corn hybrids",
            "Rotate crops with non-host plants",
            "Till infected crop debris after harvest",
        ],
    ),
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": DiseaseInfo(
        name="Gray Leaf Spot",
        name_ar="تبقع الأوراق الرمادي",
        plant="Corn",
        severity="high",
        description="Fungal disease causing rectangular grey lesions on corn leaves.",
        treatments=[
            "Apply Strobilurin fungicide",
            "Spray at tasseling stage",
            "Repeat every 14 days",
        ],
        prevention=[
            "Plant resistant hybrids",
            "Reduce crop residue through tillage",
            "Rotate with soybeans or other crops",
        ],
    ),
    "Tomato___Bacterial_spot": DiseaseInfo(
        name="Bacterial Spot",
        name_ar="التبقع البكتيري",
        plant="Tomato",
        severity="high",
        description="Bacterial disease causing water-soaked spots on leaves and fruit.",
        treatments=[
            "Apply copper bactericide immediately",
            "Remove infected plant material",
            "Avoid working with wet plants",
        ],
        prevention=[
            "Use certified disease-free seeds",
            "Avoid overhead irrigation",
            "Rotate crops every 2-3 years",
        ],
    ),
    "Tomato___Septoria_leaf_spot": DiseaseInfo(
        name="Septoria Leaf Spot",
        name_ar="تبقع سيبتوريا",
        plant="Tomato",
        severity="medium",
        description="Fungal disease causing small circular spots with dark borders.",
        treatments=[
            "Apply Chlorothalonil or Mancozeb",
            "Remove infected lower leaves",
            "Spray every 7-10 days",
        ],
        prevention=[
            "Avoid overhead watering",
            "Mulch around base of plants",
            "Rotate crops annually",
        ],
    ),
    "Tomato___Spider_mites Two-spotted_spider_mite": DiseaseInfo(
        name="Spider Mites",
        name_ar="العناكب الحمراء",
        plant="Tomato",
        severity="medium",
        description="Pest infestation causing stippled yellow leaves and webbing.",
        treatments=[
            "Apply Neem oil or insecticidal soap",
            "Spray water forcefully on undersides of leaves",
            "Apply Abamectin miticide if severe",
        ],
        prevention=[
            "Maintain adequate soil moisture",
            "Avoid excessive nitrogen",
            "Introduce predatory mites",
        ],
    ),
    "Tomato___Target_Spot": DiseaseInfo(
        name="Target Spot",
        name_ar="التبقع الهدفي",
        plant="Tomato",
        severity="medium",
        description="Fungal disease causing concentric ring spots on leaves.",
        treatments=[
            "Apply Chlorothalonil fungicide",
            "Remove infected leaves",
            "Spray every 7 days",
        ],
        prevention=[
            "Ensure good air circulation",
            "Avoid overhead irrigation",
            "Rotate crops regularly",
        ],
    ),
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": DiseaseInfo(
        name="Yellow Leaf Curl Virus",
        name_ar="فيروس تجعد الأوراق الصفراء",
        plant="Tomato",
        severity="high",
        description="Viral disease spread by whiteflies causing yellowing and curling.",
        treatments=[
            "Remove and destroy infected plants",
            "Control whitefly population with insecticides",
            "No chemical cure for the virus",
        ],
        prevention=[
            "Use virus-resistant tomato varieties",
            "Control whiteflies with yellow sticky traps",
            "Use reflective mulches to repel whiteflies",
        ],
    ),
    "Tomato___Tomato_mosaic_virus": DiseaseInfo(
        name="Tomato Mosaic Virus",
        name_ar="فيروس موزاييك الطماطم",
        plant="Tomato",
        severity="high",
        description="Viral disease causing mosaic patterns and distorted leaves.",
        treatments=[
            "Remove and destroy infected plants immediately",
            "Disinfect tools with bleach solution",
            "No chemical cure available",
        ],
        prevention=[
            "Use certified virus-free seeds",
            "Wash hands before handling plants",
            "Control aphid vectors",
        ],
    ),
}


def get_disease_info(class_name: str) -> DiseaseInfo:
    """Get disease information by class name."""
    return DISEASE_DATABASE.get(
        class_name,
        DiseaseInfo(
            name=class_name.replace("_", " "),
            name_ar="غير معروف",
            plant="Unknown",
            severity="medium",
            description="Disease information not available.",
            treatments=["Consult a local agricultural expert"],
            prevention=["Monitor plant regularly"],
        ),
    )


def get_severity_color(severity: str) -> str:
    """Return color code based on severity."""
    colors = {
        "low": "#22c55e",
        "medium": "#f97316", 
        "high": "#ef4444",
    }
    return colors.get(severity, "#888888")


SUPPORTED_PLANTS = list({info.plant for info in DISEASE_DATABASE.values()})
ALL_CLASSES = list(DISEASE_DATABASE.keys())