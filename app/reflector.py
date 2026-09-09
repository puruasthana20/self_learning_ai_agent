from app.state import AgentState


class Reflector:

    def reflect(self, state: AgentState):

        failed_steps = []

        for step_name, result in state.tool_results.items():

            if isinstance(result, dict):

                if result.get("success") is False:

                    failed_steps.append(step_name)

        if failed_steps:

            state.reflection = (
                f"Execution failed at: {', '.join(failed_steps)}"
            )

            state.confidence = 0.0

        else:

            state.reflection = "Execution completed successfully."

            state.confidence = 1.0

        return state