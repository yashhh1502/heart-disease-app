import joblib
import os

def load_model():
    # Get absolute path to model file
    model_path = os.path.join(os.path.dirname(__file__), "..", "model", "logistic.pkl")
    
    model = joblib.load(model_path)
    return model