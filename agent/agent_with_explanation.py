from agent.risk_agent import assess_project_risk
from llm.explanation_engine import build_explanation_prompt, explain_with_llm

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

agent_result = assess_project_risk(sample_project)

prompt = build_explanation_prompt(sample_project, agent_result)
explanation = explain_with_llm(prompt)

print("=== AGENT DECISION ===")
print(agent_result)
print("\n=== LLM EXPLANATION ===")
print(explanation)
