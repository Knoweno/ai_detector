import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Replace with your OpenAI API key
openai.api_key = os.getenv("OPENAI_SECRET_KEY")

def chatbot_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if using GPT-3.5
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].message['content'].strip()

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
