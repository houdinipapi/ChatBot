from transformers import pipeline

def tranformer_bot():
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
    print("Hello! I'm a transformer bot.\nType 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        # Generate a response
        response = chatbot(
            user_input,
            max_length=50,
            num_return_sequences=1,
            truncation=True
        )
        print(f"Bot: {response[0]['generated_text']}")

if __name__ == "__main__":
    tranformer_bot()
