import io
import contextlib


def python_executor(code: str) -> str:
    """
    Executes Python code and captures its output.
    """

    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})

        result = output.getvalue()

        if result.strip():
            return result.strip()

        return "Code executed successfully."

    except Exception as e:
        return f"Python Execution Error: {e}"