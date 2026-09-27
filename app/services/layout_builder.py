from app.ai.gemini_flash import (
    generate_comic_story
)

from app.ai.gemini_pro import (
    improve_prompt
)

from app.ai.image_generator import (
    generate_image
)


def build_comic(
    story_prompt,
    character_name,
    setting,
    tone,
    art_style
):

    comic = generate_comic_story(
        story_prompt=story_prompt,
        character_name=character_name,
        setting=setting,
        tone=tone,
        art_style=art_style
    )


    for panel in comic["panels"]:

        original_prompt = (
            panel["image_prompt"]
        )


        improved_prompt = improve_prompt(
            original_prompt
        )


        panel["image_prompt"] = (
            improved_prompt
        )


        try:

            panel["image_url"] = (
                generate_image(
                    improved_prompt
                )
            )

        except Exception:

            panel["image_url"] = None


    return comic