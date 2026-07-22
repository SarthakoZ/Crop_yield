import pandas as pd
import joblib
import streamlit as st

model = joblib.load("crop_yield_prediction_model.pkl")

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="centered"
)

st.title("Crop Yield Prediction")
st.subheader( "• Enter all details and click Predict.")

with st.sidebar:
    st.title("Crop Yield Prediction")
    st.divider()
    
    st.markdown("""
    **🌾 Crop Yield Prediction**
    Crop Yield Prediction is a machine learning application that predicts crop yield using agricultural, soil, weather, and farming data.
    **Model:** Linear Regression
    **Average Cross-Validation R² Score:** 0.6764
    """)

    st.text("• Model : Linear Regression")
    st.write("• R² Score : 0.6764 (Average Cross-Validation R²)")

col1 , col2, col3, col4 = st.columns(4)

with col1:
    st.text("• Crop Information")

    state = st.selectbox(
        "Select your State",
        ["maharashtra", "west bengal", "karnataka", "odisha", "bihar", "punjab"]
    )

    district_options = {
        "maharashtra": ["pune"],
        "west bengal": ["purulia"],
        "karnataka": ["mysuru"],
        "odisha": ["cuttack"],
        "bihar": ["patna"],
        "punjab": ["ludhiana"]
    }

    district = st.selectbox(
        "Select your District",
        district_options[state]
    )

    season = st.selectbox(
        "Season",
        ["rabi", "kharif", "zaid"]
    )

    crop_options = {
        "rabi": ["mustard", "wheat", "potato"],
        "kharif": ["rice", "maize", "cotton"],
        "zaid": ["sugarcane"]
    }

    crop = st.selectbox(
        "Crop",
        crop_options[season]
    )

with col2:
    st.text("• Soil Information")
    soil_options = {
        "maharashtra": ["black", "red", "loamy"],
        "west bengal": ["clay", "loamy"],
        "karnataka": ["red", "black"],                                             
        "odisha": ["clay", "red"],
        "bihar": ["loamy", "clay"],
        "punjab": ["loamy", "clay"]
    }

    soil_type = st.selectbox(
        "Choose Soil Type",
        soil_options[state]
    )

    nitrogen = st.number_input("Enter amount of nitrogen : ")
    phosphorus = st.number_input("Enter amount of phosphorus : ")
    potassium = st.number_input("Enter amount of potassium : ")

with col3:
    st.text("• Weather Conditions")
    rainfall = st.number_input(" Enter rainfall in mm : ")
    temperature = st.number_input("Enter temperature in c : ")
    humidity = st.number_input("Enter humidity : ")

with col4:
    st.text("• Farming Details")
    area_hectare = st.number_input("Enter area in hectare : ")
    fertilizer_used =  st.number_input("Enter amount of fertilizer used : ")
    irrigation = st.selectbox("Enter irrigation status : ", ["yes", "no"])

if st.button("🌾 Predict Crop Yield", use_container_width=True):
    try:
        input_data = pd.DataFrame([{
            "state": state,
            "district": district,
            "crop": crop,
            "season": season,
            "area_hectare": area_hectare,
            "rainfall_mm": rainfall,
            "temperature_c": temperature,
            "humidity": humidity,
            "soil_type": soil_type,
            "nitrogen": nitrogen,
            "phosphorus": phosphorus,
            "potassium": potassium,
            "fertilizer_used": fertilizer_used,
            "irrigation": irrigation
        }])

        pred = model.predict(input_data)

        st.success(f"Predicted Crop Yield: {pred[0]} ton/hectare")
        with st.expander("View Submitted Details"):
            st.dataframe(input_data)

    except Exception as e:
        st.error(e)

comparison = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "Random Forest Regressor",
        "XGBoost Regressor"
    ],
    "Average R² Score": [
        0.6764,
        0.6324,
        0.6040
    ],
    "Status": [
        "Selected",
        "Evaluated",
        "Evaluated"
    ]
})

st.table(comparison)

st.info(
"""
Linear Regression was selected as the final model because it achieved
the highest average R² score (0.6764) among all evaluated regression models.
"""
)