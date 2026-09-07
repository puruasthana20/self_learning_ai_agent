from app.state import AgentState
from app.llm import LLMService
from app.prompts import PLANNER_PROMPT
import json


class Planner:

    def __init__(self):
        self.llm = LLMService()

    def create_plan(self, state: AgentState):

        prompt = f"""
{PLANNER_PROMPT}

User Request:
{state.user_input}
"""

        response = self.llm.generate(prompt)

        print(response)

        return state