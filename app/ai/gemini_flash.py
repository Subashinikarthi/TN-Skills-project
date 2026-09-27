import json

from app.ai.gemini_client import client

from app.config import (
    TEXT_MODEL
)


def clean_json(text: str) -> str:

    text = text.strip()

    if text.startswith("```json"):

        text = text[7:]

    elif text.startswith("```"):

        text = text[3:]

    if text.endswith("```"):

        text = text[:-3]

    return text.strip()


def generate_comic_story(
    story_prompt,
    character_name,
    setting,
    tone,
    art_style
):

    prompt = f"""
You are an experienced generative AI
comic project developer and comic writer.

Create a complete four-panel comic.

Story idea:
{story_prompt}

Main character:
{character_name}

Setting:
{setting}

Tone:
{tone}

Art style:
{art_style}

Requirements:

1. Create exactly four panels.
2. All four panels must form one continuous story.
3. Give each panel a scene.
4. Give each panel narration.
5. Give each panel dialogue.
6. Give each panel a detailed image prompt.
7. Keep the main character visually consistent.
8. Do not add unnecessary characters.

Return ONLY valid JSON.

Use exactly this structure:

{{
    "title": "Comic title",

    "summary": "Short summary",

    "panels": [

        {{
            "panel_number": 1,
            "scene": "Scene description",
            "narration": "Narration",
            "dialogue": "Dialogue",
            "image_prompt": "Detailed image prompt"
        }},

        {{
            "panel_number": 2,
            "scene": "Scene description",
            "narration": "Narration",
            "dialogue": "Dialogue",
            "image_prompt": "Detailed image prompt"
        }},

        {{
            "panel_number": 3,
            "scene": "Scene description",
            "narration": "Narration",
            "dialogue": "Dialogue",
            "image_prompt": "Detailed image prompt"
        }},

        {{
            "panel_number": 4,
            "scene": "Scene description",
            "narration": "Narration",
            "dialogue": "Dialogue",
            "image_prompt": "Detailed image prompt"
        }}

    ]
}}
"""

    response = client.models.generate_content(
        model=TEXT_MODEL,
        contents=prompt
    )

    if not response.text:

        raise RuntimeError(
            "Gemini returned an empty response."
        )

    cleaned = clean_json(
        response.text
    )

    return json.loads(cleaned)