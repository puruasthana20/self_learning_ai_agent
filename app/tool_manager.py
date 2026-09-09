from app.tools.echo_tool import echo_tool
from app.tools.pdf_reader import pdf_reader
from app.tools.summarizer import summarizer
from app.tools.calculator import calculator
from app.tools.web_search import web_search
from app.tools.file_writer import file_writer
from app.tools.memory_store import memory_store
from app.tools.memory_search import memory_search
from app.tools.python_executor import python_executor


class ToolManager:

    def __init__(self):

        self.tools = {
            "echo": echo_tool,
            "pdf_reader": pdf_reader,
            "summarizer": summarizer,
            "calculator": calculator,
            "web_search": web_search,
            "file_writer": file_writer,
            "memory_store": memory_store,
            "memory_search": memory_search,
            "python_executor": python_executor,
        }

    def execute(self, tool_name: str, args: dict):

        if tool_name not in self.tools:
            raise ValueError(f"Unknown tool: {tool_name}")

        tool = self.tools[tool_name]

        return tool(**args)