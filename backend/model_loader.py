import os
import joblib

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "..", "model", "logistic.pkl")
    return joblib.load(model_path)