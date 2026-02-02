import joblib
import numpy as np

model = joblib.load("model/loan_model.pkl")
scaler = joblib.load("model/scaler.pkl")

def predict_loan(age, income, credit_score, loan_amount):
    X = np.array([[age, income, credit_score, loan_amount]])
    X_scaled = scaler.transform(X)
    pred = model.predict(X_scaled)[0]
    return "Approved" if pred == 1 else "Rejected"