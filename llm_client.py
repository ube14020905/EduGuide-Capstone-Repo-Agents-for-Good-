# llm_client.py
import os
import json
import asyncio


class LLMClient:
  def __init__(self, mode='mock'):
    self.mode = mode
# mode: mock | openai | gemini


  async def generate_text(self, prompt: str, context: str = ""):
# Mock implementation for offline demo. Replace with real LLM calls.
    if self.mode == 'mock':
      await asyncio.sleep(0.2)
# Very simple mock: echo a trimmed prompt and supply dummy quiz
      if 'Generate 3 concise questions' in prompt:
        return "[\n {\"id\":1, \"q\": \"What is X?\", \"type\": \"short\"},\n {\"id\":2, \"q\": \"Choose Y\", \"type\": \"mcq\", \"options\": [\"A\", \"B\", \"C\"]},\n {\"id\":3, \"q\": \"Compute Z\", \"type\": \"short\"}\n]"
      if 'Score the' in prompt:
        return json.dumps({"score": 0.8, "feedback": "Good attempt — check step 2."})
# lesson generation fallback
      return f"Lesson (mock) on: {prompt[:120]}"
    else:
# Placeholder for real LLM clients (OpenAI / Gemini). Do not include API keys here.
      raise NotImplementedError("Please implement real LLM calls for mode=openai or mode=gemini")
