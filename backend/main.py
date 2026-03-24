from fastapi import FastAPI
from pydantic import BaseModel
from predict import make_prediction

app = FastAPI()

# -------- INPUT SCHEMA -------- #
class PatientData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int


# -------- HOME ROUTE -------- #
@app.get("/")
def home():
    return {"message": "Heart Disease Prediction API Running"}


# -------- PREDICT ROUTE -------- #
@app.post("/predict")
def predict(data: PatientData):
    
    # 🔍 Debug print (VERY useful)
    print("Received data:", data)

    # Convert to dict and send to model
    pred, prob = make_prediction(data.dict())

    # Return response
    return {
        "prediction": pred,
        "probability": round(prob * 100, 2),
        "message": "Heart Disease Detected" if pred == 1 else "No Heart Disease"
    }