AVAILABLE_TOOLS = """
Available tools:

1. echo
Arguments:
- text (string)

Description:
Returns the input text unchanged.
Useful for responding directly to the user.

----------------------------

2. pdf_reader
Arguments:
- pdf_path (string)

Description:
Reads a PDF file and returns its extracted text.

----------------------------

3. summarizer
Arguments:
- text (string)

Description:
Creates a concise summary of the provided text.

----------------------------

4. calculator
Arguments:
- expression (string)

Description:
Evaluates a mathematical expression and returns the result.

----------------------------

5. web_search
Arguments:
- query (string)

Description:
Searches the web for information.

----------------------------

6. file_writer
Arguments:
- file_path (string)
- content (string)

Description:
Writes the provided content into a file.

----------------------------

7. memory_store
Arguments:
- key (string)
- value (string)

Description:
Stores useful long-term information about the user.

Examples:
name → Puru
city → Delhi
favorite_language → Python
favorite_editor → VS Code
dream_company → OpenAI

Use this only when the user shares information that will likely be useful in future conversations.

----------------------------

8. memory_search
Arguments:
- key (string)

Description:
Retrieves previously stored information from memory.

Examples:
name
city
favorite_language

----------------------------

9. python_executor
Arguments:
- code (string)

Description:
Executes Python code and returns the output.
"""