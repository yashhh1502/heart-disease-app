import streamlit as st

# 🔥 ADD THESE IMPORTS (IMPORTANT)
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.predict import make_prediction


# -------- PAGE CONFIG -------- #
st.set_page_config(page_title="Heart Disease Predictor", layout="centered")

# -------- CUSTOM CSS -------- #
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #e63946;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #e63946;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 50px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# -------- HEADER -------- #
st.markdown('<div class="title">❤️ Heart Disease Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered health risk analysis</div>', unsafe_allow_html=True)

st.divider()

# -------- INPUT FORM -------- #
with st.form("prediction_form"):

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("👤 Age", min_value=1, max_value=120, value=None, placeholder="Enter age")
        sex = st.selectbox("⚧ Sex", ["Select", "Female", "Male"])
        cp = st.selectbox("💓 Chest Pain Type", ["Select", 0,1,2,3])
        trestbps = st.number_input("🩺 Blood Pressure", min_value=80, max_value=200, value=None)

        chol = st.number_input("🧪 Cholesterol", min_value=100, max_value=400, value=None)
        fbs = st.selectbox("🍬 Blood Sugar >120", ["Select", 0,1])

    with col2:
        restecg = st.selectbox("📈 ECG Result", ["Select", 0,1,2])
        thalach = st.number_input("❤️ Max Heart Rate", min_value=60, max_value=220, value=None)
        exang = st.selectbox("🏃 Exercise Angina", ["Select", 0,1])
        oldpeak = st.number_input("📉 ST Depression", min_value=0.0, max_value=6.0, value=None)

        slope = st.selectbox("📊 Slope", ["Select", 0,1,2])
        ca = st.selectbox("🧬 Major Vessels", ["Select", 0,1,2,3])
        thal = st.selectbox("🧪 Thalassemia", ["Select", 0,1,2,3])

    submit = st.form_submit_button("🔍 Predict")

# -------- PROCESS -------- #
if submit:

    # Convert values
    sex = 0 if sex == "Female" else 1 if sex == "Male" else None
    cp = None if cp == "Select" else int(cp)
    fbs = None if fbs == "Select" else int(fbs)
    restecg = None if restecg == "Select" else int(restecg)
    exang = None if exang == "Select" else int(exang)
    slope = None if slope == "Select" else int(slope)
    ca = None if ca == "Select" else int(ca)
    thal = None if thal == "Select" else int(thal)

    # Validation
    if None in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]:
        st.error("⚠️ Please fill all fields properly")
    
    else:
        data = {
            "age": int(age),
            "sex": sex,
            "cp": cp,
            "trestbps": int(trestbps),
            "chol": int(chol),
            "fbs": fbs,
            "restecg": restecg,
            "thalach": int(thalach),
            "exang": exang,
            "oldpeak": float(oldpeak),
            "slope": slope,
            "ca": ca,
            "thal": thal
        }

        with st.spinner("🔄 Analyzing patient data..."):
            # 🔥 DIRECT FUNCTION CALL (NO API)
            pred, prob = make_prediction(data)

            result = {
                "prediction": pred,
                "probability": round(prob * 100, 2),
                "message": "Heart Disease Detected" if pred == 1 else "No Heart Disease"
            }

        st.divider()
        st.subheader("🧾 Prediction Result")

        st.success(result["message"])
        st.info(f"Confidence: {result['probability']}%")

        # Risk Level
        prob = result["probability"]

        if prob < 30:
            st.success("🟢 Low Risk")
        elif prob < 70:
            st.warning("🟡 Medium Risk")
        else:
            st.error("🔴 High Risk")

        # Progress bar
        st.progress(int(prob))

        # Advice
        if result["prediction"] == 1:
            st.warning("⚠️ Consult a doctor. Maintain healthy lifestyle.")
        else:
            st.success("✅ You are in a healthy range. Keep it up!")