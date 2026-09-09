from app.agent import Agent


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