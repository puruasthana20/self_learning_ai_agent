import os


def file_writer(file_path: str, content: str) -> str:
    """
    Writes content to a file.
    Creates the directory if it does not exist.
    """

    try:
        directory = os.path.dirname(file_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Successfully wrote to '{file_path}'."

    except Exception as e:
        return f"File Write Error: {e}"