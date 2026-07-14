from app.llm import ask_llm

answer = ask_llm(
    "Create one short beginner piano exercise for practicing finger numbers."
)

print(answer)