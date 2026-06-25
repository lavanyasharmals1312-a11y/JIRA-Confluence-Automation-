import os
import json


from pathlib import Path

OUTPUT_FOLDER = (
    Path(__file__).resolve().parents[1] / "outputs"
)


def load_latest_project():

    files = [
        f for f in os.listdir(OUTPUT_FOLDER)
        if f.startswith("project_") and f.endswith(".json")
    ]

    if not files:
        return None

    files.sort()

    latest = files[-1]

    filepath = os.path.join(
        OUTPUT_FOLDER,
        latest
    )

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)