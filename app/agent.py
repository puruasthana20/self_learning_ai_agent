from app.state import AgentState
from app.planner import Planner


class Agent:

    def __init__(self):
        self.planner = Planner()

    def run(self, user_input: str):

        state = AgentState(
            user_input=user_input,
            goal=user_input
        )

        state = self.planner.create_plan(state)

        return state