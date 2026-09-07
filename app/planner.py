from app.state import AgentState
from app.llm import LLMService
from app.prompts import PLANNER_PROMPT
import json

class Planner:
    def create_plan(self, state: AgentState):
        state.plan = [
            "Understand the task",
            "Identify required tools",
            "Execute tools",
            "Generate final answer"
        ]

        return state