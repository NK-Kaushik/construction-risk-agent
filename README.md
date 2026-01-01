# 🏗️ AI Construction Project Delay & Cost Overrun Risk Agent

## 📌 Overview

Construction projects frequently suffer from **schedule delays** and **cost overruns**, even though large amounts of project data are available. The challenge is not data availability, but **making proactive, explainable decisions early enough**.

This project implements an **AI-powered decision support system** that:

* Predicts **delay risk** and **cost overrun risk** using machine learning
* Uses an **AI agent** to reason over these risks and determine escalation severity
* Generates **human-readable explanations** using an LLM
* Exposes the system via a **FastAPI REST API** for real-world integration

⚠️ This system is designed for **decision support**, not autonomous control, and keeps humans firmly **in the loop**.

---

## 🎯 Key Capabilities

* 📊 **ML-based risk prediction** for construction projects
* 🤖 **AI agent reasoning** for escalation and action decisions
* 🧠 **LLM-based explainability** for transparency and trust
* 🌐 **REST API** for integration with dashboards and tools
* 🧩 Modular, production-style architecture

---

## 🛠️ Tech Stack

| Layer    | Technology                                         |
| -------- | -------------------------------------------------- |
| Language | Python                                             |
| ML       | Scikit-learn (Random Forest)                       |
| AI Agent | Rule-based decision logic                          |
| LLM      | Prompt-based explanation layer (provider-agnostic) |
| API      | FastAPI                                            |
| Server   | Uvicorn                                            |

---

## 📁 Project Structure

```
construction-ai-risk-agent/
│
├── data/                 # Synthetic construction project data
├── models/               # Trained ML models and label encoders
├── agent/                # AI agent logic and reasoning
├── llm/                  # LLM explanation layer
├── api/                  # FastAPI service
├── notebooks/            # EDA and analysis
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2️⃣ Start the API

```bash
python -m uvicorn api.main:app --reload
```

### 3️⃣ Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 🔌 Example API Request

```json
{
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
```

---

## 📤 Example API Response

```json
{
  "delay_risk": "High",
  "cost_overrun_risk": "Medium",
  "escalation_level": "WARNING",
  "recommended_action": "Investigate root causes and prepare mitigation plan.",
  "explanation": "The project shows elevated delay risk due to slower-than-expected progress and material delivery delays..."
}
```

---

# 🧠 What I Built — Step by Step (Detailed Explanation)

This section explains **what I did, why I did it, and what each step achieves**.

---

## STEP 1 — Project Setup & Structure

### What I Did

* Created a modular repository structure separating:

  * Data
  * Models
  * Agent logic
  * LLM explanations
  * API layer

### Why I Did This

* Mirrors **real production AI systems**
* Keeps responsibilities clearly separated
* Makes the project scalable and maintainable

### What This Achieves

* Clean imports
* Easier testing
* Interview-ready architecture

---

## STEP 2 — Construction Domain Signals & Dataset

### What I Did

* Identified **real construction KPIs**:

  * Project progress
  * Labor availability
  * Material delays
  * Budget consumption
  * Change orders
* Generated **synthetic but domain-faithful data**
* Created delay and cost risk labels using rule-based logic

### Why I Did This

* Real construction data is proprietary
* Synthetic data allows safe experimentation
* Domain-faithful logic ensures realistic patterns

### What This Achieves

* Meaningful ML training data
* Transparent label generation
* Interview-safe dataset design

---

## STEP 3 — Exploratory Data Analysis (EDA)

### What I Did

* Analyzed distributions of delay and cost risk
* Verified correlations between:

  * Progress vs delay risk
  * Budget usage vs cost risk
  * External disruptions vs delays

### Why I Did This

* ML models should **never be trained blindly**
* EDA validates that labels align with real-world intuition

### What This Achieves

* Confidence in data quality
* Prevents garbage-in / garbage-out modeling
* Strong ML engineering practice

---

## STEP 4 — Machine Learning Risk Models

### What I Did

* Trained two **Random Forest classifiers**:

  * Delay risk model
  * Cost overrun risk model
* Evaluated precision, recall, and F1-score
* Saved trained models and encoders

### Why I Did This

* Tree-based models work well on tabular operational data
* Balance performance and interpretability
* Suitable for downstream decision systems

### What This Achieves

* Reliable early risk detection
* Explainable predictions
* Reusable prediction components

---

## STEP 5 — AI Agent (Decision & Reasoning Layer)

### What I Did

* Built an AI agent that:

  * Consumes ML predictions
  * Applies business rules
  * Determines escalation severity
  * Recommends actions

### Why I Did This

* ML predicts patterns, but **does not decide**
* Organizational policies should not be learned statistically
* Decision logic must be auditable and controllable

### What This Achieves

* True **agentic behavior**
* Human-in-the-loop safety
* Clear separation of prediction vs decision

---

## STEP 6 — LLM Explanation Layer

### What I Did

* Designed structured prompts for explanations
* Used the LLM **only for communication**, not decisions
* Generated concise, actionable explanations

### Why I Did This

* Stakeholders need **trust and transparency**
* LLMs are best used for explanation, not control
* Prevents hallucination and unsafe autonomy

### What This Achieves

* Human-readable reasoning
* Improved decision confidence
* Enterprise-safe LLM usage

---

## STEP 7 — FastAPI REST Service

### What I Did

* Wrapped the AI agent in a FastAPI service
* Defined input/output schemas
* Exposed a clean `/assess-risk` endpoint
* Ran it using Uvicorn

### Why I Did This

* Real AI systems are accessed via APIs
* Enables integration with dashboards and tools
* Mirrors production ML inference services

### What This Achieves

* Deployable AI system
* Standard HTTP interface
* End-to-end usable product

---

## 🧩 System Design Philosophy

* ML → **Pattern detection**
* AI Agent → **Decision reasoning**
* LLM → **Explanation**
* API → **Integration**
* Human → **Final authority**

This separation ensures **safety, explainability, and scalability**.

