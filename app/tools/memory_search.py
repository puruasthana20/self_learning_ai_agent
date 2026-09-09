import json
import os

MEMORY_FILE = "memory.json"


def memory_search(key: str) -> str:
    """
    Searches for a value in memory.json by its key.
    """

    try:
        if not os.path.exists(MEMORY_FILE):
            return "Memory is empty."

        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            memory = json.load(file)

        return memory.get(key, f"No memory found for key '{key}'.")

    except Exception as e:
        return f"Memory Search Error: {e}"