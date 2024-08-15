# Diabetes Prediction Using LSTM Model

## Project Overview

### Problem Statement
Diabetes is a chronic condition affecting how the body processes blood sugar (glucose). Predicting diabetes risk can aid in early diagnosis and management. This project aims to develop an application that predicts diabetes risk using an LSTM (Long Short-Term Memory) model, which excels in handling sequential and time series data.

### Objective
- Develop an LSTM model to predict diabetes risk.
- Build a Flask backend to serve the model.
- Create a Streamlit frontend for user interaction.

## Team Members
This project was developed by:
- Manarth Patel
- Shriram Yadav
- Manu Shrivastava
- Rakshay Patel
- Miraj Sutariya

## Dataset
- **diabetes_prediction_dataset.csv**: Contains patient data with features like age, BMI, glucose levels, etc.
- **AML_fp.ipynb**: Jupyter Notebook for data preprocessing, exploratory analysis, and feature engineering.

## Model Development

### LSTM Model
The core of the project is the LSTM model, which captures temporal dependencies in the data. The model is saved in:
- **backend/lstm_model.keras**: Trained LSTM model in Keras format.

### Backend Implementation
The backend is implemented using Flask, which provides an API to interact with the LSTM model. The backend code is in:
- **backend/app.py**: Flask application and API endpoints.

## Frontend Implementation
The frontend is built using Streamlit, offering an interactive interface for users. The frontend code is in:
- **frontend/app.py**: Streamlit application.


## Application Structure


The project directory is organized as follows:

```plaintext
backend/
   └── app.py
   └── lstm_model.keras
dataset/
   └── AML_fp.ipynb
   └── diabetes_prediction_dataset.csv
frontend/
   └── app.py
.gitignore
README.md
aml_final.png
git-flow.docx
predictions.json
requirements.txt
'''

### Files Description
- **backend/app.py**: Flask backend for predictions.
- **backend/lstm_model.keras**: Trained LSTM model.
- **dataset/AML_fp.ipynb**: Data processing and analysis.
- **dataset/diabetes_prediction_dataset.csv**: Training dataset.
- **frontend/app.py**: Streamlit frontend application.
- **.gitignore**: Specifies files and directories to ignore.
- **README.md**: Project overview and details.
- **aml_final.png**: Screenshot of the final application.
- **git-flow.docx**: Git workflow document.
- **predictions.json**: Sample predictions output.
- **requirements.txt**: Required Python packages.

## Implementation Details

### Data Preprocessing
Data is cleaned and prepared for modeling, including handling missing values, feature scaling, and dataset splitting.

### Model Training
The LSTM model is trained with the dataset. Model parameters, training, and performance metrics are monitored to ensure accuracy.

### Backend API
Flask serves as the backend, handling API requests, loading the model, and providing predictions.

### Frontend Interface
Streamlit provides a user-friendly interface for inputting data and viewing predictions.

## Results

### Model Performance
The LSTM model achieved 97% accuracy, demonstrating its effectiveness in predicting diabetes risk.

### User Interface
The frontend application is designed to be intuitive and accessible for users.

### Final Deliverables
- **aml_final.png**: Final application interface screenshot.
- **predictions.json**: Example model predictions.

## Conclusion
The Diabetes Prediction Using LSTM Model project successfully delivered a high-performance diabetes prediction application with a robust backend and user-friendly frontend.

## Future Work
Future improvements may include:
- Adding more features or data sources.
- Deploying the application on a cloud platform.
- Implementing user authentication and data analysis features.

