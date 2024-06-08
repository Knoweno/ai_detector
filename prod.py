import openai

# Replace with your OpenAI API key
openai.api_key = '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'

def chatbot_prompt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can change this to "gpt-4" if available
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the AI-powered Insurance Chatbot!")
    print("You can ask any questions related to your insurance needs.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Thank you for using the AI-powered Insurance Chatbot. Goodbye!")
            break

        response = chatbot_prompt(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

