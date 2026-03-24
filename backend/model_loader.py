import joblib   # use joblib (safer)

def load_model():
    model = joblib.load("../model/logistic.pkl")
    return model