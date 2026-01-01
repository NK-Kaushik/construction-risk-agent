from fastapi import FastAPI
from pydantic import BaseModel

from agent.risk_agent import assess_project_risk
from llm.explanation_engine import build_explanation_prompt, explain_with_llm

app = FastAPI(
    title="AI Construction Risk Agent",
    description="Predicts delay and cost overrun risk and provides AI-driven explanations",
    version="1.0"
)

# ---- Input Schema ---- #

class ProjectData(BaseModel):
    planned_duration_days: int
    days_elapsed: int
    actual_progress_pct: float
    labor_availability: float
    subcontractor_delay: int
    weather_delay_days: int
    material_delay_days: int
    cost_spent_pct: float
    change_orders: int


# ---- API Endpoint ---- #

@app.post("/assess-risk")
def assess_risk(project: ProjectData):
    project_dict = project.dict()

    agent_result = assess_project_risk(project_dict)

    prompt = build_explanation_prompt(project_dict, agent_result)
    explanation = explain_with_llm(prompt)

    return {
        **agent_result,
        "explanation": explanation
    }
