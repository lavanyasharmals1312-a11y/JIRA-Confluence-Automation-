import os
import json


from pathlib import Path

OUTPUT_FOLDER = (
    Path(__file__).resolve().parents[1] / "outputs"
)


def save_project(project_data):

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    existing = [
        f for f in os.listdir(OUTPUT_FOLDER)
        if f.startswith("project_") and f.endswith(".json")
    ]

    next_number = len(existing) + 1

    filename = f"project_{next_number:03}.json"

    filepath = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            project_data,
            file,
            indent=4
        )

    return {

    "project": project_data,

    "filepath": filepath

}