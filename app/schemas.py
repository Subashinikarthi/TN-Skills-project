from typing import List, Optional

from pydantic import BaseModel, Field


class ComicRequest(BaseModel):

    story_prompt: str = Field(
        ...,
        min_length=3
    )

    character_name: str = "Alex"

    setting: str = "Modern city"

    tone: str = "Funny"

    art_style: str = "Comic book"


class Panel(BaseModel):

    panel_number: int

    scene: str

    narration: str

    dialogue: str

    image_prompt: str

    image_url: Optional[str] = None


class ComicResponse(BaseModel):

    title: str

    summary: str

    panels: List[Panel]