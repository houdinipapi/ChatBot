def simple_echo_bot():
    print("Hello! I am a simple echo bot.\nType 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        print(f"Bot: {user_input}")


if __name__ == "__main__":
    simple_echo_bot()