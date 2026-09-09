"""from app.agent import Agent


def main():

    print("Inside main()")

    agent = Agent()

    print("Agent created")

    state = agent.run(
        user_input="Summarize this PDF",
        pdf_path="data/sample.pdf"
    )

    print("\nReturned from run()\n")

    print("Final Answer:\n")
    print(state.final_answer)


if __name__ == "__main__":
    main()

 """
"""   

from app.agent import Agent


def main():

    agent = Agent()

    state = agent.run(
        user_input="My favorite programming language is Python."
    )

    print("\nFINAL ANSWER")
    print(state.final_answer)

    print("\nMEMORY")
    print(state.retrieved_memories)


if __name__ == "__main__":
    main()

"""

from app.agent import Agent


def main():

    agent = Agent()

    state = agent.run(
        user_input="What is my favorite programming language?"
    )

    print(state.final_answer)


if __name__ == "__main__":
    main()