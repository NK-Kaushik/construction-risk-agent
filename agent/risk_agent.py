import os
import joblib
import pandas as pd
from agent.reasoning_rules import determine_escalation, recommended_action
from .reasoning_rules import determine_escalation, recommended_action


# Resolve model paths dynamically
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

delay_model = joblib.load(os.path.join(MODEL_DIR, "delay_risk_model.pkl"))
cost_model = joblib.load(os.path.join(MODEL_DIR, "cost_risk_model.pkl"))

delay_encoder = joblib.load(os.path.join(MODEL_DIR, "delay_label_encoder.pkl"))
cost_encoder = joblib.load(os.path.join(MODEL_DIR, "cost_label_encoder.pkl"))

FEATURES = [
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


def assess_project_risk(project_data: dict):
    df = pd.DataFrame([project_data])[FEATURES]

    delay_pred = delay_model.predict(df)[0]
    cost_pred = cost_model.predict(df)[0]

    delay_risk = delay_encoder.inverse_transform([delay_pred])[0]
    cost_risk = cost_encoder.inverse_transform([cost_pred])[0]

    escalation = determine_escalation(delay_risk, cost_risk)
    action = recommended_action(escalation)

    return {
        "delay_risk": delay_risk,
        "cost_overrun_risk": cost_risk,
        "escalation_level": escalation,
        "recommended_action": action
    }
