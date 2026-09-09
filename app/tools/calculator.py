import math


def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression safely.
    """

    allowed_names = {
        "abs": abs,
        "round": round,
        "min": min,
        "max": max,
        "pow": pow,
        "sqrt": math.sqrt,
        "ceil": math.ceil,
        "floor": math.floor,
        "pi": math.pi,
        "e": math.e,
    }

    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)

    except Exception as e:
        return f"Calculation Error: {e}"