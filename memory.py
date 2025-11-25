# memory.py
from typing import Dict, Any, List


class MemoryBank:
  def __init__(self):
    self.profiles: Dict[str, Dict[str, Any]] = {}
    self.sessions: Dict[str, List[Dict[str, Any]]] = {}
    self.interactions: List[Dict[str, Any]] = []


  def get_profile(self, student_id: str) -> Dict[str, Any]:
    return self.profiles.get(student_id, {"mastery": 0.2})


  def update_profile(self, student_id: str, updates: Dict[str, Any]):
    p = self.profiles.get(student_id, {"mastery": 0.2})
    p.update(updates)
    self.profiles[student_id] = p


  def create_session(self, student_id: str, session: Dict[str, Any]):
    self.sessions.setdefault(student_id, []).append(session)


  def retrieve_context(self, student_id: str, topic: str) -> str:
# For prototype, return last session lesson for the topic
    user_sessions = self.sessions.get(student_id, [])
    for s in reversed(user_sessions):
      if s.get("topic") == topic:
        return s.get("lesson", "")
    return ""


  def log_interaction(self, student_id: str, data: Dict[str, Any]):
    self.interactions.append({"student_id": student_id, **data})
