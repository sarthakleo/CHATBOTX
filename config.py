import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    raise EnvironmentError(
        "GROQ_API_KEY not found. "
        "Create a .env file with: GROQ_API_KEY=gsk_..."
    )

MODEL: str = "llama-3.3-70b-versatile"
MAX_TOKENS: int = 1024
TEMPERATURE: float = 0.7

APP_TITLE: str = " Course Advisor"
APP_ICON: str = "book"
APP_CAPTION: str = "Ask me about fees, syllabus, batches, or enrollment"
WELCOME_MESSAGE: str = (
    "Hi! I'm your  course advisor. "
    "Ask me about fees, syllabus, duration, "
    "batch dates, or how to enroll."
)
QUICK_QUESTIONS: list[str] = [
    "What courses do you offer?",
    "What is the AI/ML bootcamp fee?",
    "When does the next batch start?",
    "Is EMI available?",
    "What does the Data Science course cover?",
    "How do I enroll?",
]
