"""from app.agent import Agent

def main():
    print("Inside main()")

    agent = Agent()

    print("Agent created")

    state = agent.run("Summarize this PDF")

    print("Returned from run()")

    print(state)


if __name__ == "__main__":
    main()"""

from app.llm import LLMService

def main():
    llm = LLMService()

    answer = llm.generate(
        "In one sentence, what is an AI agent?"
    )

    print(answer)


if __name__ == "__main__":
    main()