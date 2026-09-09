from app.tools.echo_tool import echo_tool
from app.tools.pdf_reader import pdf_reader


class ToolManager:

    def __init__(self):

        self.tools = {
            "echo": echo_tool,
            "pdf_reader": pdf_reader
        }

    def execute(self, tool_name: str, input_data: str):

        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name}")

        tool = self.tools[tool_name]

        return tool(input_data)