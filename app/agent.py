from app.state import AgentState
from app.planner import Planner
from app.executor import Executor
from app.responder import Responder
from app.reflector import Reflector


class Agent:

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.responder = Responder()
        self.reflector = Reflector()

    def run(self, user_input: str, pdf_path: str = ""):

        state = AgentState(
            user_input=user_input,
            goal=user_input,
            pdf_path=pdf_path
        )

        state = self.planner.create_plan(state)

        state = self.executor.execute(state)

        state = self.reflector.reflect(state)

        state = self.responder.generate_response(state)

        return state