def build_explanation_prompt(project_data, agent_result):
    return f"""
You are an AI assistant supporting a construction project manager.

Project Signals:
- Planned Duration (days): {project_data['planned_duration_days']}
- Days Elapsed: {project_data['days_elapsed']}
- Actual Progress (%): {project_data['actual_progress_pct']}
- Labor Availability: {project_data['labor_availability']}
- Material Delay Days: {project_data['material_delay_days']}
- Weather Delay Days: {project_data['weather_delay_days']}
- Cost Spent (%): {project_data['cost_spent_pct']}
- Change Orders: {project_data['change_orders']}

Risk Assessment:
- Delay Risk: {agent_result['delay_risk']}
- Cost Overrun Risk: {agent_result['cost_overrun_risk']}
- Escalation Level: {agent_result['escalation_level']}

Explain:
1. Why the project has this risk level
2. What signals contributed most
3. Suggested mitigation steps
Keep the explanation concise and actionable.
"""


def explain_with_llm(prompt):
    """
    Placeholder for LLM call.
    Replace with OpenAI / Azure / local LLM later.
    """
    return (
        "The project shows elevated delay risk due to slower-than-expected progress "
        "relative to elapsed time and significant material delays. Cost risk is rising "
        "because a large portion of the budget has already been spent while progress remains low. "
        "It is recommended to investigate material supply bottlenecks, reassess subcontractor schedules, "
        "and review cost controls to prevent escalation."
    )
