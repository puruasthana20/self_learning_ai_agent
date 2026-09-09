from app.state import AgentState
from app.planner import Planner
from app.executor import Executor
from app.reflector import Reflector
from app.responder import Responder
from app.memory.retriever import MemoryRetriever


class Agent:

    def __init__(self):

        self.memory_retriever = MemoryRetriever()
        self.planner = Planner()
        self.executor = Executor()
        self.reflector = Reflector()
        self.responder = Responder()

    def run(self, user_input: str, pdf_path: str = ""):

        state = AgentState(
            user_input=user_input,
            goal=user_input,
            pdf_path=pdf_path
        )

        # 1. Retrieve relevant memories
        state = self.memory_retriever.retrieve(state)

        # 2. Create plan
        state = self.planner.create_plan(state)

        # 3. Execute plan
        state = self.executor.execute(state)

        # 4. Reflect
        state = self.reflector.reflect(state)

        # 5. Generate final response
        state = self.responder.respond(state)

        return state