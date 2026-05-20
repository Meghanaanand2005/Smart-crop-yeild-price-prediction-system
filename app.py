import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/best_model.pkl")

# Page configuration
st.set_page_config(
    page_title="🌾 Crop Price Prediction",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #e8f5e9, #ffffff);
}
.big-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #2e7d32;
}
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #555;
}
.prediction-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #dcedc8;
    border: 2px solid #7cb342;
    text-align: center;
    font-size: 30px;
    font-weight: bold;
    color: #1b5e20;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="big-title">🌾 Smart Crop Price Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Predict crop price using Machine Learning</div>', unsafe_allow_html=True)

st.write("")
st.write("### 📝 Enter Crop and Soil Details")

# Input layout
col1, col2 = st.columns(2)

with col1:
    n_soil = st.number_input("🌱 Nitrogen (N_SOIL)", value=50.0)
    p_soil = st.number_input("🧪 Phosphorus (P_SOIL)", value=40.0)
    k_soil = st.number_input("🌿 Potassium (K_SOIL)", value=40.0)
    temperature = st.number_input("🌡 Temperature (°C)", value=25.0)
    humidity = st.number_input("💧 Humidity (%)", value=70.0)

with col2:
    ph = st.number_input("⚗ Soil pH", value=6.5)
    rainfall = st.number_input("🌧 Rainfall (mm)", value=120.0)
    state = st.selectbox("📍 State", [
        "Karnataka", "Maharashtra", "Tamil Nadu",
        "Andhra Pradesh", "Kerala"
    ])
    crop = st.selectbox("🌾 Crop", [
        "Rice", "Wheat", "Maize", "Cotton", "Sugarcane"
    ])

# Predict button
if st.button("🔮 Predict Crop Price", use_container_width=True):
    input_data = pd.DataFrame([{
        "N_SOIL": n_soil,
        "P_SOIL": p_soil,
        "K_SOIL": k_soil,
        "TEMPERATURE": temperature,
        "HUMIDITY": humidity,
        "ph": ph,
        "RAINFALL": rainfall,
        "STATE": state,
        "CROP": crop
    }])

    prediction = model.predict(input_data)[0]

    st.write("")
    st.markdown(
        f'<div class="prediction-box">💰 Predicted Crop Price: ₹ {prediction:,.2f}</div>',
        unsafe_allow_html=True
    )

    st.balloons()

# Footer
st.write("---")
st.caption("Built with Python, Scikit-learn, XGBoost, and Streamlit")