# Heart Risk Predictor Web App

## Overview
A machine learning web application that predicts cardiovascular 
risk from patient health data using Linear Regression, 
deployed as a Flask web application.

## Dataset
- File: cardio_dataset.csv
- Features (7 inputs): age, gender, and other cardiovascular 
  health indicators
- Target: cardiovascular risk score (continuous)
- Train/Test Split: 80/20

## Model Details
- Algorithm: Linear Regression (scikit-learn)
- Evaluation: R² Score
- Model coefficients and intercept extracted after training
- Saved model: heart_risk_Linear_regression.sav (joblib)

## Why Linear Regression?
The target variable (risk score) is continuous, making 
Linear Regression a natural and interpretable choice 
for this prediction task.

## Tech Stack
- Python 3.9
- scikit-learn (LinearRegression, train_test_split, r2_score)
- Pandas, NumPy (data processing)
- Flask (web application deployment)
- joblib (model saving/loading)
- Jupyter Notebook

## Project Structure
heart-risk-predictor/
├── dataset_creation.ipynb   # Model training notebook
├── heart_risk_predictor.py  # Flask web application
├── cardio_dataset.csv       # Dataset
└── templates/               # HTML templates for web UI

## How to Run
1. Clone this repository
2. Install requirements:
   pip install flask scikit-learn pandas numpy joblib
3. First run the notebook to train and save the model:
   jupyter notebook dataset_creation.ipynb
4. Then start the Flask app:
   python heart_risk_predictor.py
5. Open browser: http://localhost:5000
6. Enter patient health data and get risk prediction

## Author
Kavindya Hewage | Abu Dhabi, UAE
LinkedIn: linkedin.com/in/kavindya-sureshi-8b39681b8/
GitHub: github.com/KAVINDYASURESHI
Portfolio: https://KAVINDYASURESHI.github.io
