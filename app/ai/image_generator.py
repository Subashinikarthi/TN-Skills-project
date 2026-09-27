import os
import uuid

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from app.config import PANELS_DIR


load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")


def generate_image(prompt):

    if not HF_TOKEN:
        raise RuntimeError(
            "HF_TOKEN is missing from .env"
        )

    client = InferenceClient(
        provider="auto",
        api_key=HF_TOKEN
    )

    image = client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-schnell"
    )

    filename = (
        "panel_"
        + uuid.uuid4().hex
        + ".png"
    )

    filepath = os.path.join(
        PANELS_DIR,
        filename
    )

    image.save(filepath)

    return (
        "/static/panels/"
        + filename
    )