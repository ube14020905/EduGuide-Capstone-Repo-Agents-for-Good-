# EduGuide — Personalized Learning Companion (Agents for Good)


**Track:** Agents for Good — Google × Kaggle 5-Day AI Agents Intensive Capstone


**Summary**
EduGuide is a lightweight multi-agent tutoring system designed for low-resource classrooms. It creates short adaptive micro-lessons, quizzes students, updates long-term memory, and provides teacher-facing summaries.


## Features
- Multi-agent design: Planner, Tutor, Retriever (in Tutor), Evaluator.
- Tools: LLM wrapper, local FAISS-compatible memory (stub), grading sandbox.
- Sessions & Memory: per-session state + long-term MemoryBank.
- Observability: structured logging and a metrics endpoint stub.
- Evaluation: pre/post test protocol and A/B testing design (described below).

## Repo Structure
eduguide-capstone/
├── README.md
├── requirements.txt
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── orchestrator.py
├── planner_agent.py
├── tutor_agent.py
├── llm_client.py
├── memory.py
├── utils.py
├── notebooks/
│ └── demo_notebook.md
└── diagrams/
└── architecture.mmd

## Quick start (local, dev)


1. Create virtualenv and install dependencies


```bash
python -m venv venv
source venv/bin/activate # Windows: venv\\Scripts\\activate
pip install -r requirements.txt 
```
2.Run the orchestrator
```bash
export EDUGUIDE_MODEL=mock    # set to 'mock' for local dev; replace with 'gemini' or 'openai' when configured
uvicorn orchestrator:app --reload --port 8000
```
3.Start a session (example using curl)
```bash
curl -X POST http://localhost:8000/start_session -H "Content-Type: application/json" -d '{"student_id":"alice","topic":"fractions"}'
