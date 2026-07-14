from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-5.4-mini",   # or qwen2.5:7b, mistral, etc.
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content