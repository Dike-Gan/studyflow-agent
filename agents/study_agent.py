import os

from skills.summary_skill import generate_summary
from skills.flashcard_skill import generate_flashcards


class StudyAgent:
    def __init__(self, model: str = "llama3"):
        self.model = model

    def run(self, text: str) -> None:
        os.makedirs("outputs", exist_ok=True)

        summary = generate_summary(text, self.model)
        flashcards = generate_flashcards(text, self.model)

        with open("outputs/summary.md", "w", encoding="utf-8") as f:
            f.write(summary)

        with open("outputs/flashcards.csv", "w", encoding="utf-8") as f:
            f.write(flashcards)