# Heart Risk Predictor Web App

A machine learning web app that estimates cardiovascular risk (%) from 7 patient health details, built in two versions to compare approaches: a Linear Regression baseline (v1) and a Keras neural network (v2). Both are served through a Flask web app.

> Educational project. Not medical advice and not a diagnostic tool.

## Versions

| Version | Model | Folder | R² (20% hold-out) |
|---|---|---|---|
| v1 | Linear Regression (scikit-learn) | `v1-linear-regression/` 
| v2 | Feedforward neural network (Keras) | `v2-neural-network/` | 0.86 |

## Dataset

- File: `cardio_dataset.csv`
- 7 input features: gender (0 = male, 1 = female), age, total cholesterol (mg/dL), HDL (mg/dL), smoker (1/0), blood pressure medication (1/0), diabetes (1/0)
- Target: cardiovascular risk score (continuous, shown as a %)
- Train/test split: 80/20

## v1: Linear Regression (`v1-linear-regression/`)

- scikit-learn `LinearRegression`, evaluated with R²; coefficients and intercept extracted after training
- The target is continuous, so Linear Regression is a natural, interpretable baseline
- Model saved with joblib as `heart_risk_Linear_regression.sav` (created when you run the notebook)

## v2: Neural Network (`v2-neural-network/`)

- Inputs and target scaled with `MinMaxScaler`; predictions are inverse-scaled back to a risk %
- Architecture: Dense 128 → 64 → 10 (sigmoid) → 1 (linear), dropout 0.5 after the first two layers, 9,941 parameters
- Adam optimizer, MSE loss, 200 epochs; best checkpoint kept by validation loss (epoch 180, saved as `models/model-180.keras`)
- R² = 0.86 on the 20% validation split. The same split was used to pick the checkpoint, so treat this as slightly optimistic.

## Tech Stack

- Python 3.9
- scikit-learn, TensorFlow/Keras
- Pandas, NumPy, Matplotlib
- Flask
- joblib
- Jupyter Notebook

## Project Structure

- `v1-linear-regression/`
  - `dataset_creation.ipynb`: model training notebook
  - `heart_risk_predictor.py`: Flask app
  - `cardio_dataset.csv`: dataset
  - `templates/`: HTML templates
- `v2-neural-network/`
  - `FFNN-HRP.ipynb`: model training notebook
  - `main.py`: Flask app
  - `models/`: trained model (`model-180.keras`) and fitted scalers (`scaler_data.sav`, `scaler_target.sav`)
  - `templates/`: HTML templates (`patient_details.html`, `patient_results.html`)

## How to Run

### v1
1. Clone this repository
2. `pip install flask scikit-learn pandas numpy joblib`
3. `cd v1-linear-regression`
4. Train and save the model: `jupyter notebook dataset_creation.ipynb`
5. Start the app: `python heart_risk_predictor.py`
6. Open http://localhost:5000 and enter the patient details

### v2
1. Clone this repository
2. `pip install flask tensorflow keras scikit-learn joblib numpy` (tested with Python 3.9, Keras 3.10, scikit-learn 1.6.1, TensorFlow , Flask)
3. `cd v2-neural-network`
4. Start the app: `python main.py` (the trained model and scalers are included, so no retraining is needed)
5. Open http://127.0.0.1:5000 and enter the patient details

To retrain v2, run `FFNN-HRP.ipynb` (it needs `cardio_dataset.csv` in the same folder), move the two scaler files into `models/`, and update the model filename in `main.py` to the new best-checkpoint epoch.

## Author

Kavindya Hewage | Abu Dhabi, UAE
LinkedIn: linkedin.com/in/kavindya-sureshi-8b39681b8/ | GitHub: github.com/KAVINDYASURESHI | Portfolio: https://KAVINDYASURESHI.github.io

