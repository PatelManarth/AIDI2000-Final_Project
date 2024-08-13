import streamlit as st
import requests
import numpy as np
import pandas as pd

st.title('Diabetes Prediction')

# Input fields
gender = st.selectbox('Gender', ['Female', 'Male'])
age = st.number_input('Age', min_value=0)
hypertension = st.selectbox('Hypertension', [0, 1])
heart_disease = st.selectbox('Heart Disease', [0, 1])
smoking_history = st.selectbox('Smoking History', ['never', 'No Info'])
bmi = st.number_input('BMI', min_value=0.0)
HbA1c_level = st.number_input('HbA1c Level', min_value=0.0)
blood_glucose_level = st.number_input('Blood Glucose Level', min_value=0.0)

# Convert categorical features to numerical values if needed
gender = 1 if gender == 'Male' else 0
smoking_history = 0 if smoking_history == 'never' else 1

# Predict button
if st.button('Predict'):
    features = {
        'features': [
            gender, age, hypertension, heart_disease,
            smoking_history, bmi, HbA1c_level, blood_glucose_level
        ]
    }

    response = requests.post('http://localhost:5000/predict', json=features)

    try:
        prediction = response.json()['prediction']
        st.write(f'Prediction: {"Diabetes" if prediction == 1 else "No Diabetes"}')
    except ValueError:
        st.write('Error: Unable to decode JSON from the response.')

# Show all predictions button
if st.button('Show All Predictions'):
    response = requests.get('http://localhost:5000/predictions')

    try:
        predictions = response.json()
        if predictions:
            # Create a DataFrame for better display
            df = pd.DataFrame(predictions)
            df.index += 1  # Start the index at 1 instead of 0
            st.table(df)
        else:
            st.write('No predictions available yet.')
    except ValueError:
        st.write('Error: Unable to decode JSON from the response.')
