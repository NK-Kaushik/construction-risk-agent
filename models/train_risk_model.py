import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv(r"C:\Users\keert\Desktop\Git Projects\construction-risk-agent\data\project_data.csv")

# Features used for modeling
feature_cols = [
    "planned_duration_days",
    "days_elapsed",
    "actual_progress_pct",
    "labor_availability",
    "subcontractor_delay",
    "weather_delay_days",
    "material_delay_days",
    "cost_spent_pct",
    "change_orders"
]

X = df[feature_cols]

# Encode labels
le_delay = LabelEncoder()
le_cost = LabelEncoder()

y_delay = le_delay.fit_transform(df["delay_risk"])
y_cost = le_cost.fit_transform(df["cost_overrun_risk"])

# Train-test split
X_train, X_test, y_delay_train, y_delay_test = train_test_split(
    X, y_delay, test_size=0.2, random_state=42
)

_, _, y_cost_train, y_cost_test = train_test_split(
    X, y_cost, test_size=0.2, random_state=42
)

# Train models
delay_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
delay_model.fit(X_train, y_delay_train)

cost_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
cost_model.fit(X_train, y_cost_train)

# Evaluate
print("Delay Risk Model Performance")
print(classification_report(y_delay_test, delay_model.predict(X_test)))

print("\nCost Overrun Risk Model Performance")
print(classification_report(y_cost_test, cost_model.predict(X_test)))

# Save models
joblib.dump(delay_model, "models/delay_risk_model.pkl")
joblib.dump(cost_model, "models/cost_risk_model.pkl")
joblib.dump(le_delay, "models/delay_label_encoder.pkl")
joblib.dump(le_cost, "models/cost_label_encoder.pkl")

print("Models saved in models/")
