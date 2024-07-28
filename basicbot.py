import nltk
from nltk.tokenize import word_tokenize


def nltk_bot():
    print("Hello! I'm an NLTK bot.\nType 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        tokens = word_tokenize(user_input)
        print(f"Bor: You said {len(tokens)} words: {tokens}")


if __name__ == "__main__":
    nltk_bot()