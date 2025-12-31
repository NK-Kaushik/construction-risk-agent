from agent.risk_agent import assess_project_risk

sample_project = {
    "planned_duration_days": 300,
    "days_elapsed": 180,
    "actual_progress_pct": 40,
    "labor_availability": 0.7,
    "subcontractor_delay": 1,
    "weather_delay_days": 12,
    "material_delay_days": 25,
    "cost_spent_pct": 65,
    "change_orders": 6
}

result = assess_project_risk(sample_project)
print(result)
