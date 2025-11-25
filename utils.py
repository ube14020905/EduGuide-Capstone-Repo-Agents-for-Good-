# utils.py
import json


def safe_parse_json(s: str):
  try:
    return json.loads(s)
  except Exception:
    return {"raw": s}
