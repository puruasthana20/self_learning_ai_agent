from app.llm import LLMService


def summarizer(text: str) -> str:
    """
    Summarizes the given text using the configured LLM.
    """

    llm = LLMService()

    prompt = f"""
You are an expert summarizer.

Summarize the following text in a clear and concise way.

Text:
{text}
"""

    summary = llm.generate(prompt)

    return summary