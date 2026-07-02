from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required by the OpenAI client, ignored by Ollama
)


def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama3.2:3b",   # or qwen2.5:7b, mistral, etc.
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content