from app.state import AgentState
from app.llm import LLMService
from app.prompts import PLANNER_PROMPT
from app.tool_catalog import AVAILABLE_TOOLS
import json


class Planner:

    def __init__(self):
        self.llm = LLMService()

    def create_plan(self, state: AgentState):

        prompt = f"""
{PLANNER_PROMPT}

{AVAILABLE_TOOLS}

Relevant Memories:
{state.retrieved_memories}

Current State

PDF Path:
{state.pdf_path}

User Request:
{state.user_input}
"""

        print("\n========== PROMPT ==========\n")
        print(prompt)
        print("\n============================\n")

        response = self.llm.generate(prompt)

        data = json.loads(response)

        state.plan = data["steps"]

        print(response)

        return state