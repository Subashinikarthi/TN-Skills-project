from fastapi import (
    APIRouter,
    HTTPException,
    Request
)

from fastapi.responses import JSONResponse

from app.schemas import ComicRequest

from app.services.layout_builder import (
    build_comic
)

from app.services.exporters import (
    export_comic
)

from app.ai.image_generator import (
    generate_image
)


router = APIRouter()


@router.get("/")
async def home(request: Request):

   return request.app.state.templates.TemplateResponse(
    request,
    "index.html",
    {
        "request": request
    }
)


@router.get("/comic-preview")
async def comic_preview(request: Request):

    return request.app.state.templates.TemplateResponse(
    request,
    "comic_preview.html",
    {
        "request": request
    }
)


@router.post("/generate-comic/json")
async def generate_comic_json(
    data: ComicRequest
):

    try:

        comic = build_comic(
            story_prompt=data.story_prompt,
            character_name=data.character_name,
            setting=data.setting,
            tone=data.tone,
            art_style=data.art_style
        )

        return JSONResponse(
            content=comic
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@router.post("/generate")
async def generate(
    data: ComicRequest
):

    try:

        comic = build_comic(
            story_prompt=data.story_prompt,
            character_name=data.character_name,
            setting=data.setting,
            tone=data.tone,
            art_style=data.art_style
        )

        return JSONResponse(
            content=comic
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@router.post("/test-image")
async def test_image(data: dict):

    prompt = data.get("prompt")

    if not prompt:

        raise HTTPException(
            status_code=400,
            detail="Image prompt is required."
        )

    try:

        image_url = generate_image(
            prompt
        )

        return {
            "success": True,
            "image_url": image_url
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@router.post("/export-success")
async def export_success(
    request: Request,
    data: dict
):

    comic = data.get("comic")

    if not comic:

        raise HTTPException(
            status_code=400,
            detail="Comic data is required."
        )

    try:

        file_url = export_comic(
            comic
        )

        return request.app.state.templates.TemplateResponse(
    request,
    "export_success.html",
    {
        "request": request,
        "file_url": file_url
    }
)

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )