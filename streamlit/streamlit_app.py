import streamlit as st
import joblib
import pandas as pd
import numpy as np
import os
from pathlib import Path

# Load the trained model and scaler
@st.cache_resource
def load_model_and_scaler():
    """Load model and scaler from multiple possible locations"""
    
    # Define possible paths to search for model files
    possible_paths = [
        # Current directory
        Path('.'),
        # Script directory
        Path(__file__).parent,
        # Parent directory (in case app is in subdirectory)
        Path(__file__).parent.parent,
        # Streamlit subdirectory
        Path(__file__).parent / 'streamlit',
        # Root of repository
        Path(__file__).parent.parent / 'streamlit',
    ]
    
    model_file = None
    scaler_file = None
    
    # Search for model files
    for base_path in possible_paths:
        model_path = base_path / 'logistic_regression_model.joblib'
        scaler_path = base_path / 'scaler.joblib'
        
        if model_path.exists() and scaler_path.exists():
            model_file = model_path
            scaler_file = scaler_path
            break
    
    # If files not found, show helpful error message
    if model_file is None or scaler_file is None:
        st.error("""
        ### Model files not found!
        
        Please ensure the following files are in the same directory as `streamlit_app.py`:
        - `logistic_regression_model.joblib`
        - `scaler.joblib`
        
        **To generate these files:**
        1. Run `python train_model.py` in your project directory
        2. Upload the generated `.joblib` files to your GitHub repository
        3. Make sure they're in the same folder as `streamlit_app.py`
        
        **Current search paths:**
        """)
        for p in possible_paths:
            st.write(f"- {p.absolute()}")
        st.stop()
    
    # Load the model and scaler
    try:
        model = joblib.load(model_file)
        scaler = joblib.load(scaler_file)
        return model, scaler
    except Exception as e:
        st.error(f"Error loading model files: {str(e)}")
        st.stop()

model, scaler = load_model_and_scaler()

st.set_page_config(page_title="Diabetes Prediction App", layout="centered")
st.title("🏥 Diabetes Prediction App")
st.write("Please enter the patient's details to predict the likelihood of diabetes.")

# Sidebar for user input
st.sidebar.header('Patient Data Input')

def user_input_features():
    pregnancies = st.sidebar.slider('Pregnancies', 0, 17, 3) # Min: 0, Max: 17, Default: 3 (from df.describe() mean/median)
    glucose = st.sidebar.slider('Glucose (mg/dL)', 44.0, 199.0, 117.0) # Min: 44, Max: 199, Default: 117 (from median)
    blood_pressure = st.sidebar.slider('Blood Pressure (mmHg)', 24.0, 122.0, 72.0) # Min: 24, Max: 122, Default: 72 (from median)
    skin_thickness = st.sidebar.slider('Skin Thickness (mm)', 7.0, 99.0, 29.0) # Min: 7, Max: 99, Default: 29 (from median)
    insulin = st.sidebar.slider('Insulin (mu U/ml)', 14.0, 846.0, 125.0) # Min: 14, Max: 846, Default: 125 (from median)
    bmi = st.sidebar.slider('BMI', 18.2, 67.1, 32.3) # Min: 18.2, Max: 67.1, Default: 32.3 (from median)
    dpf = st.sidebar.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.372) # Min: 0.078, Max: 2.42, Default: 0.372 (from median)
    age = st.sidebar.slider('Age (years)', 21, 81, 29) # Min: 21, Max: 81, Default: 29 (from median)

    data = {
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('User Input:')
st.write(input_df)

# Scale the input features
input_scaled = scaler.transform(input_df)

# Make prediction
prediction_proba = model.predict_proba(input_scaled)[:, 1]
prediction = (prediction_proba > 0.5).astype(int)

st.subheader('Prediction Result:')
if prediction[0] == 1:
    st.error(f"⚠️ The patient is predicted to be **Diabetic** with a probability of **{prediction_proba[0]:.2%}**")
else:
    st.success(f"✅ The patient is predicted to be **Non-Diabetic** with a probability of **{(1 - prediction_proba[0]):.2%}**")

st.subheader('Prediction Probability:')
col1, col2 = st.columns(2)
with col1:
    st.metric("Diabetes Risk", f"{prediction_proba[0]:.2%}")
with col2:
    st.metric("Non-Diabetes", f"{(1 - prediction_proba[0]):.2%}")

st.markdown("""
--- 
**About this app:**
This application uses a Logistic Regression model trained on the Pima Indians Diabetes Database to predict the likelihood of diabetes based on patient health metrics.

**Disclaimer:** This is a predictive tool for educational purposes only and should not be used as a substitute for professional medical advice.
""")
