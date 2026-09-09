from duckduckgo_search import DDGS


def web_search(query: str) -> str:
    """
    Searches the web using DuckDuckGo and returns
    the top search results.
    """

    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return "No search results found."

        output = []

        for result in results:
            output.append(
                f"Title: {result['title']}\n"
                f"URL: {result['href']}\n"
                f"Body: {result['body']}\n"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Search Error: {e}"