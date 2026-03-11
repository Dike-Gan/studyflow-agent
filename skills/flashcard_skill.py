import ollama


def generate_flashcards(text: str, model: str = "llama3") -> str:
    prompt = f"""
Create 5 study flashcards from the following text.

Requirements:
- Focus on key concepts
- Keep answers short and clear
- Output ONLY in CSV format
- Use this exact format:

Question,Answer
What is X?,X is ...
Why is Y important?,Y is important because ...

Text:
{text}
"""

    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]