import pandas as pd
import numpy as np

np.random.seed(42)
n_projects = 500

data = {
    "planned_duration_days": np.random.randint(90, 720, n_projects),
    "days_elapsed": np.random.randint(30, 600, n_projects),
    "actual_progress_pct": np.random.uniform(10, 95, n_projects),

    "labor_availability": np.random.uniform(0.5, 1.0, n_projects),
    "subcontractor_delay": np.random.randint(0, 2, n_projects),

    "weather_delay_days": np.random.randint(0, 30, n_projects),
    "material_delay_days": np.random.randint(0, 45, n_projects),

    "cost_spent_pct": np.random.uniform(20, 100, n_projects),
    "change_orders": np.random.randint(0, 15, n_projects),
}

df = pd.DataFrame(data)

# ---- Risk Label Logic ---- #

def assign_delay_risk(row):
    time_ratio = row["days_elapsed"] / row["planned_duration_days"]
    progress_gap = time_ratio * 100 - row["actual_progress_pct"]

    if progress_gap > 30 or row["material_delay_days"] > 20:
        return "High"
    elif progress_gap > 15 or row["weather_delay_days"] > 10:
        return "Medium"
    else:
        return "Low"

def assign_cost_risk(row):
    if row["cost_spent_pct"] > row["actual_progress_pct"] + 30:
        return "High"
    elif row["cost_spent_pct"] > row["actual_progress_pct"] + 15:
        return "Medium"
    else:
        return "Low"

df["delay_risk"] = df.apply(assign_delay_risk, axis=1)
df["cost_overrun_risk"] = df.apply(assign_cost_risk, axis=1)

df.to_csv("data/project_data.csv", index=False)

print("Dataset created: data/project_data.csv")
