import json
import os

MEMORY_FILE = "memory.json"


def memory_store(key: str, value: str) -> str:
    """
    Stores a key-value pair in memory.json.
    """

    try:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                memory = json.load(file)
        else:
            memory = {}

        memory[key] = value

        with open(MEMORY_FILE, "w", encoding="utf-8") as file:
            json.dump(memory, file, indent=4)

        return f"Memory stored under key '{key}'."

    except Exception as e:
        return f"Memory Store Error: {e}"