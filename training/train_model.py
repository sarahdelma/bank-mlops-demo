import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv("data/sample_data.csv")

X = data[['age', 'income', 'credit_score', 'loan_amount']]
y = data['approved']

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_scaled, y)

# Save artifacts (MLOps concept)
joblib.dump(model, "model/loan_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")