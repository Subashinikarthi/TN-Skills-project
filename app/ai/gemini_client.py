from google import genai

from app.config import GEMINI_API_KEY


if not GEMINI_API_KEY:

    raise RuntimeError(
        "GEMINI_API_KEY is missing. "
        "Please create a .env file and add your Gemini API key."
    )


client = genai.Client(
    api_key=GEMINI_API_KEY
)