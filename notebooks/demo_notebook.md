# EduGuide — Demo Notebook (Kaggle-Friendly)

This notebook demonstrates a minimal working example of the EduGuide multi-agent tutoring system.

You can convert this markdown into a `.ipynb` on Kaggle by creating Markdown + Code cells.

---

## 1. Introduction

This demo shows:

1. Starting a tutoring session with the **Planner Agent** + **Tutor Agent**  
2. Viewing the generated lesson + quiz  
3. Submitting answers for evaluation  
4. Updating student memory  
5. Computing a simple learning gain metric  

For the demo, we will load the Python modules directly instead of calling the FastAPI server.

---

## 2. Setup

```python
# Install dependencies (only needed on Kaggle)
!pip install fastapi uvicorn pydantic sentence-transformers faiss-cpu numpy
# Import project modules (adjust paths if needed)
from planner_agent import PlannerAgent
from tutor_agent import TutorAgent
from llm_client import LLMClient
from memory import MemoryBank
```

## 3.Initialize Agents
```python
memory = MemoryBank()
llm = LLMClient(mode="mock")   # mock mode for demo
planner = PlannerAgent(memory)
tutor = TutorAgent(memory, llm)
```

## 4.Start a Session
```python
student_id = "alice"
topic = "fractions"

plan = planner.create_plan(student_id, topic)
session = await tutor.run_lesson(student_id, plan)

plan, session
```

## Expected output:
1. A 15-minute micro-lesson
2. 3 generated quiz questions
3. Lesson context stored in memory

## 5. Display Lesson + Quiz
```python
print("=== LESSON ===\\n")
print(session["lesson"])

print("\\n=== QUIZ ===\\n")
print(session["quiz"])
```
## 6. Simulate Student Answers
```python
sample_answers = [
    {"student_id": "alice", "question_id": 1, "answer": "The numerator"},
    {"student_id": "alice", "question_id": 2, "answer": "Option B"},
    {"student_id": "alice", "question_id": 3, "answer": "1/2"},
]

results = []
for ans in sample_answers:
    res = await tutor.evaluate_answer(ans)
    results.append(res)

results
```
## 7. Learning Gain Calculation (Synthetic Example)
```python
pretest = 0.40
posttest = 0.70

normalized_gain = (posttest - pretest) / (1 - pretest)
normalized_gain
```
## 8. View Memory
```python
print("=== Memory Profile ===")
print(memory.get_profile("alice"))

print("\\n=== Sessions ===")
print(memory.sessions["alice"][:1])

print("\\n=== Interactions Logged ===")
print(memory.interactions[:3])
```
