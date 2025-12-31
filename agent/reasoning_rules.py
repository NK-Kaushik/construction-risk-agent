def determine_escalation(delay_risk, cost_risk):
    if delay_risk == "High" and cost_risk == "High":
        return "CRITICAL"
    elif delay_risk == "High" or cost_risk == "High":
        return "WARNING"
    elif delay_risk == "Medium" or cost_risk == "Medium":
        return "MONITOR"
    else:
        return "NORMAL"


def recommended_action(escalation_level):
    actions = {
        "CRITICAL": "Immediate escalation to senior management and corrective action planning.",
        "WARNING": "Investigate root causes and prepare mitigation plan.",
        "MONITOR": "Increase monitoring frequency and review weekly.",
        "NORMAL": "No action required. Continue standard tracking."
    }
    return actions.get(escalation_level, "No action defined.")
