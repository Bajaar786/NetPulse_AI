import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("equipment_logs.csv")

# Convert timestamp to datetime and set as index
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

# Define failure condition
df['failure_status'] = ((df['temperature'] > 70) & (df['usage_percentage'] > 80)).astype(int)

# Features & target
features = ["temperature", "usage_percentage", "error_rate"]
target = "failure_status"

# Normalize feature data
scaler = MinMaxScaler()
df[features] = scaler.fit_transform(df[features])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)

# Initialize and train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred))

def predict_failure(temperature, usage_percentage, error_rate):
    # Load the trained model
    model = joblib.load("models/predictive_model.pkl")

    # Normalize input features
    scaler = MinMaxScaler()
    features = np.array([[temperature, usage_percentage, error_rate]])
    features = scaler.fit_transform(features)

    # Make prediction
    prediction = model.predict(features)[0]
    return int(prediction)  # 0 = no failure, 1 = failure