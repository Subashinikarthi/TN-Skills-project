import json
import os

from datetime import datetime

from app.config import (
    REPORTS_DIR
)


def export_comic(comic):

    timestamp = (
        datetime.now()
        .strftime("%Y%m%d_%H%M%S")
    )


    filename = (
        "comic_"
        + timestamp
        + ".json"
    )


    filepath = os.path.join(
        REPORTS_DIR,
        filename
    )


    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            comic,
            file,
            indent=4,
            ensure_ascii=False
        )


    return (
        "/static/reports/"
        + filename
    )