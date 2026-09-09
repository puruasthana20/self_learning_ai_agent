from app.state import AgentState
from app.tool_manager import ToolManager


class Executor:

    def __init__(self):
        self.tool_manager = ToolManager()

    def resolve_args(self, args: dict, state: AgentState):

        resolved = {}

        for key, value in args.items():

            if isinstance(value, str):

                if value.startswith("{{step_") and value.endswith("}}"):

                    step_name = value[2:-2]      # step_1

                    step_result = state.tool_results.get(step_name, {})

                    value = step_result.get("output", "")

            resolved[key] = value

        return resolved

    def execute(self, state: AgentState):

        for index, step in enumerate(state.plan):

            args = self.resolve_args(
                step["args"],
                state
            )

            try:

                result = self.tool_manager.execute(
                    step["tool"],
                    args
                )

                state.tool_results[f"step_{index+1}"] = {
                    "success": True,
                    "tool": step["tool"],
                    "output": result
                }

            except Exception as e:

                state.tool_results[f"step_{index+1}"] = {
                    "success": False,
                    "tool": step["tool"],
                    "error": str(e)
                }

                break

            state.tool_results[f"step_{index+1}"] = result

            print(result)

        return state