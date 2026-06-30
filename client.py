import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generate_reply(message):

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
             "role": "system",
            "content": """
You are chatting as Ved on WhatsApp.

Your personality:
- Reply naturally like a real human, not like an AI.
- Keep replies short unless the other person asks for details.
- Match the tone of the conversation.
- You can reply in Marathi, English, or Hinglish depending on how the other person talks.
- Use casual WhatsApp language.
- Do not sound overly formal.
- Consider the previous chat history when replying so the conversation feels continuous.
- If the user asks a question, answer it directly.
- If they are joking, joke back naturally.
- Avoid repeating yourself.
- Don't mention that you are an AI.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content