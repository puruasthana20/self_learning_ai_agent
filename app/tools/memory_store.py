from app.memory.memory_manager import MemoryManager

memory = MemoryManager()


def memory_store(key: str, value: str):

    return memory.store(key, value)