from app.llm import LLMService


def summarizer(text: str) -> str:
    llm = LLMService()

    prompt = f"""
Summarize the following text.

{text}
"""

    summary = llm.generate(prompt)

    return summary