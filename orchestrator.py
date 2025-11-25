from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import os


from planner_agent import PlannerAgent
from tutor_agent import TutorAgent
from memory import MemoryBank
from llm_client import LLMClient


logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("eduguide")


app = FastAPI(title="EduGuide Orchestrator")


# Initialize components
memory = MemoryBank()
llm = LLMClient(mode=os.getenv("EDUGUIDE_MODEL", "mock"))
planner = PlannerAgent(memory)
tutor = TutorAgent(memory, llm)


class StartSession(BaseModel):
student_id: str
topic: str


@app.post("/start_session")
async def start_session(payload: StartSession):
logger.info({"action": "start_session", "student_id": payload.student_id, "topic": payload.topic})
plan = planner.create_plan(payload.student_id, payload.topic)
lesson = await tutor.run_lesson(payload.student_id, plan)
return {"plan": plan, "lesson": lesson}


@app.post("/submit_answer")
async def submit_answer(payload: dict):
# expecting: {student_id, question_id, answer}
if not all(k in payload for k in ("student_id", "question_id", "answer")):
raise HTTPException(status_code=400, detail="Missing fields")
result = await tutor.evaluate_answer(payload)
logger.info({"action": "submit_answer", "student_id": payload["student_id"], "result": result})
return result


@app.get("/metrics")
async def metrics():
# simple metrics stub; extend to Prometheus
return {"sessions_started": len(memory.sessions), "interactions": len(memory.interactions)}
