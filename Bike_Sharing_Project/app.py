import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('path_to_model/model.joblib')

# Function to predict bike sharing
def predict_bike_sharing(features):
    return model.predict([features])

# Streamlit app header
st.title('Bike Sharing Prediction App')

# User inputs
day_of_week = st.selectbox('Day of the Week', range(7))
hour_of_day = st.slider('Hour of the Day', min_value=0, max_value=23)
temp = st.number_input('Temperature (C)', min_value=-30.0, max_value=50.0)
humidity = st.number_input('Humidity (%)', min_value=0, max_value=100)

# Call the predict function and display the results
if st.button('Predict'):  
    features = [day_of_week, hour_of_day, temp, humidity]
    prediction = predict_bike_sharing(features)
    st.write(f'Predicted Bike Shares: {prediction[0]}')