import os
import json

from pathlib import Path


OUTPUT_FOLDER = (
    Path(__file__).resolve().parents[1] / "outputs"
)


def save_project(project_data):
    """
    Save a newly generated project.
    """

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    existing = [

        f

        for f in os.listdir(OUTPUT_FOLDER)

        if f.startswith("project_")
        and f.endswith(".json")

    ]

    next_number = len(existing) + 1

    filename = f"project_{next_number:03}.json"

    filepath = OUTPUT_FOLDER / filename

    with open(

        filepath,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            project_data,

            file,

            indent=4,

            ensure_ascii=False

        )

    return str(filepath)


def save_existing_project(
    project_data,
    filepath
):
    """
    Overwrite an existing generated project
    after edits made by the Project Manager.
    """

    with open(

        filepath,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            project_data,

            file,

            indent=4,

            ensure_ascii=False

        )

    return filepath


def get_next_project_number():

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    existing = [

        f

        for f in os.listdir(OUTPUT_FOLDER)

        if f.startswith("project_")
        and f.endswith(".json")

    ]

    return len(existing) + 1


def latest_project_filepath():

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