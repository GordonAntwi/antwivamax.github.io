
from openai import OpenAI
import os

# ✅ Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("🤖 Command Bot Ready! Type a task (or 'exit' to quit).")

while True:
    user_input = input("🧠 You: ")
    if user_input.lower() == "exit":
        print("👋 Goodbye, Gordon!")
        break

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=f"You are a GitHub automation assistant. {user_input}",
        )
        print("💬 Bot:", response.output[0].content[0].text)

    except Exception as e:
        print("⚠️ Error:", str(e))

