from app.state import AgentState


class Responder:

    def generate_response(self, state: AgentState):

        if state.confidence == 0:

            state.final_answer = state.reflection

            return state

        last_step = f"step_{len(state.tool_results)}"

        state.final_answer = state.tool_results[
            last_step
        ]["output"]

        return state