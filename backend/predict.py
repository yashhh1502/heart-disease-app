import numpy as np
from backend.model_loader import load_model
model = load_model()

def make_prediction(data: dict):
    features = np.array([[ 
        data["age"],
        data["sex"],
        data["cp"],
        data["trestbps"],
        data["chol"],
        data["fbs"],
        data["restecg"],
        data["thalach"],
        data["exang"],
        data["oldpeak"],
        data["slope"],
        data["ca"],
        data["thal"]
    ]])

    # Prediction (0 or 1)
    prediction = model.predict(features)[0]

    # Probability (confidence score)
    try:
        probability = model.predict_proba(features)[0][1]
    except:
        # fallback if model doesn't support predict_proba
        probability = 0.0

    return int(prediction), float(probability)

