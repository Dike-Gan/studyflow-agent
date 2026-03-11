from agents.study_agent import StudyAgent


def main():
    text = """
Machine learning models often suffer from overfitting when they learn noise
from training data instead of generalizable patterns.
"""

    agent = StudyAgent(model="llama3")
    agent.run(text)

    print("StudyFlow Agent finished!")
    print("Files generated: outputs/summary.md, outputs/flashcards.csv")


if __name__ == "__main__":
    main()