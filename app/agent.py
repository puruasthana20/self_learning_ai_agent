from app.state import AgentState
from app.planner import Planner
from app.tool_manager import ToolManager


class Agent:

    def __init__(self):
        self.planner = Planner()
        self.tool_manager = ToolManager()

    def run(self, user_input: str):

        state = AgentState(
            user_input=user_input,
            goal=user_input
        )

        state = self.planner.create_plan(state)

        for step in state.plan:

            result = self.tool_manager.execute(
                step["tool"],
                step["input"]
            )
            

            print(result)
        return state