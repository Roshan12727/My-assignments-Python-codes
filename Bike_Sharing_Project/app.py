import streamlit as st
import pandas as pd
import joblib
import numpy as np
import os

# Function to get user input features
def user_input_features():
    feature1 = st.number_input('Feature 1')
    feature2 = st.number_input('Feature 2')
    feature3 = st.number_input('Feature 3')
    return pd.DataFrame({'Feature 1': [feature1], 'Feature 2': [feature2], 'Feature 3': [feature3]})

# Load the model
model_path = os.path.join(os.getcwd(), 'best_random_forest.joblib')
model = joblib.load(model_path)

# Main function
def main():
    st.title('Bike Sharing Application')
    st.header('Enter the features below')

    input_df = user_input_features()

    if st.button('Predict'):
        prediction = model.predict(input_df)
        st.write('Prediction:', prediction)

if __name__ == '__main__':
    main()