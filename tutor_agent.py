# tutor_agent.py
import asyncio
from typing import Dict, Any


class TutorAgent:
def __init__(self, memory, llm_client):
self.memory = memory
self.llm = llm_client


async def run_lesson(self, student_id: str, plan: Dict[str, Any]) -> Dict[str, Any]:
# 1) Retrieve context
context = self.memory.retrieve_context(student_id, plan["topic"]) or ""
# 2) Create lesson with LLM
lesson_prompt = (
f"Create a {plan['duration_minutes']} minute micro-lesson on {plan['topic']} "
f"for difficulty {plan['difficulty']}. Include a 3-question short quiz. Keep each question concise."
)
lesson_text = await self.llm.generate_text(lesson_prompt, context=context)
# 3) Generate quiz
quiz_prompt = f"Generate 3 concise questions (MCQ or short answer) from the following lesson:\n\n{lesson_text}"
quiz = await self.llm.generate_text(quiz_prompt)
# store session
session = {
"student_id": student_id,
"topic": plan["topic"],
"lesson": lesson_text,
"quiz": quiz,
}
self.memory.create_session(student_id, session)
return session


async def evaluate_answer(self, data: Dict[str, Any]) -> Dict[str, Any]:
# data contains student_id, question_id, answer
eval_prompt = f"Score the student's answer for the question. Return a JSON: {{score:0-1, feedback: string}}.\nQuestion ID: {data['question_id']}\nAnswer: {data['answer']}"
eval_result = await self.llm.generate_text(eval_prompt)
# For mock client, llm returns a structured dict; for real clients parse accordingly
# Update memory with interaction
self.memory.log_interaction(data['student_id'], data)
# rudimentary post-processing
return {"raw_eval": eval_result}
