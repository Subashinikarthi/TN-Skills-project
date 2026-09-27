from app.ai.gemini_client import client

from app.config import (
    TEXT_MODEL
)


def improve_prompt(
    image_prompt
):

    prompt = f"""
Improve the following image prompt
for an AI generated comic panel.

Keep the original meaning.

Include:

- character appearance
- character action
- location
- background
- emotions
- lighting
- camera view
- comic art style

Do not add dialogue.

Original image prompt:

{image_prompt}
"""

    response = client.models.generate_content(
        model=TEXT_MODEL,
        contents=prompt
    )

    if not response.text:

        return image_prompt

    return response.text.strip()