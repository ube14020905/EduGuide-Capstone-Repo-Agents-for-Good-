# planner_agent.py
class PlannerAgent:
  def __init__(self, memory):
    self.memory = memory


  def create_plan(self, student_id: str, topic: str) -> dict:
    profile = self.memory.get_profile(student_id)
    mastery = profile.get("mastery", 0.2)
    difficulty = "easy" if mastery < 0.5 else "medium"
    plan = {
      "student_id": student_id,
      "topic": topic,
      "duration_minutes": 15,
      "difficulty": difficulty,
      "activities": ["explain", "example", "quiz:3"]
    }
    return plan
