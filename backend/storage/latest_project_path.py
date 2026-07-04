import os

from pathlib import Path


OUTPUT_FOLDER = (
    Path(__file__).resolve().parents[1] / "outputs"
)


def latest_project_path():

    files = [

        f

        for f in os.listdir(OUTPUT_FOLDER)

        if f.startswith("project_")
        and f.endswith(".json")

    ]

    if not files:

        return None

    files.sort()

    return OUTPUT_FOLDER / files[-1]