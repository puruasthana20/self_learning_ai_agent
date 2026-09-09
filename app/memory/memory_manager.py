import json
from pathlib import Path


class MemoryManager:

    def __init__(self):

        self.memory_file = Path("data/memory.json")

        if not self.memory_file.exists():

            self.memory_file.write_text("{}")

    def load(self):

        with open(self.memory_file, "r") as f:

            return json.load(f)

    def save(self, data):

        with open(self.memory_file, "w") as f:

            json.dump(data, f, indent=4)

    def store(self, key, value):

        memory = self.load()

        memory[key] = value

        self.save(memory)

        return f"Stored '{key}'"

    def search(self, key):

        memory = self.load()

        return memory.get(key, None)