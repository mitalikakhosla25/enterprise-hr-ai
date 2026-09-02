from pathlib import Path
import joblib
from fastapi import FastAPI
from .predictor import predict_attrition
from .analytics import (
    dashboard_summary,
    department_analysis,
    performance_analysis,
    training_analysis,
    get_employees
)
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "attrition_model.pkl"

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Enterprise HR AI",
    description="AI-powered workforce intelligence platform",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {
        "message": "Enterprise HR AI API",
        "status": "running"
    }


@app.post("/predict/attrition")
def predict(employee: dict):
    return predict_attrition(employee)
    
@app.get("/dashboard/summary")
def get_dashboard_summary():
    return dashboard_summary()


@app.get("/dashboard/departments")
def get_departments():
    return department_analysis()


@app.get("/dashboard/performance")
def get_performance():
    return performance_analysis()


@app.get("/dashboard/training")
def get_training():
    return training_analysis()

@app.get("/employees")
def employees():
    return get_employees()