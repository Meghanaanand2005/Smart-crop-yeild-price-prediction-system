# 🌾 Smart Crop Price Prediction

This project predicts crop prices using Machine Learning based on soil nutrients, weather conditions, state, and crop type.

## 🚀 Algorithms Used
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

## 📊 Model Evaluation
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Overfitting Analysis (Train vs Test R²)

## 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

## 📂 Project Structure
crop-yield-price-prediction/
├── data/
│   └── crop_yield.csv
├── notebooks/
│   └── model_training.ipynb
├── models/
│   └── best_model.pkl
├── app.py
└── requirements.txt

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
