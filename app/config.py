import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

TEXT_MODEL = os.getenv(
    "TEXT_MODEL",
    "gemini-3.5-flash-lite"
)

IMAGE_MODEL = os.getenv(
    "IMAGE_MODEL",
    "gemini-3.1-flash-image"
)

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

TEMPLATES_DIR = os.path.join(
    BASE_DIR,
    "templates"
)

STATIC_DIR = os.path.join(
    BASE_DIR,
    "static"
)

PANELS_DIR = os.path.join(
    STATIC_DIR,
    "panels"
)

REPORTS_DIR = os.path.join(
    STATIC_DIR,
    "reports"
)

os.makedirs(PANELS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)