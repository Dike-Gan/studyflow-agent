import ollama


def generate_summary(text: str, model: str = "llama3") -> str:
    prompt = f"""
Summarize the following text for a university student.

Requirements:
- Keep it clear and concise
- Highlight the most important concepts
- Use simple academic English

Text:
{text}
"""

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]