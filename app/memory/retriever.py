from app.memory.memory_manager import MemoryManager
from app.state import AgentState


class MemoryRetriever:

    def __init__(self):
        self.memory = MemoryManager()

    def retrieve(self, state: AgentState):

        memories = self.memory.load()

        relevant = []

        user_text = state.user_input.lower()

        for key, value in memories.items():

            if key.lower() in user_text:
                relevant.append(f"{key}: {value}")

        state.retrieved_memories = relevant

        return state