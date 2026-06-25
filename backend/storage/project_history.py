import os
import json


from pathlib import Path

OUTPUT_FOLDER = (
    Path(__file__).resolve().parents[1] / "outputs"
)


def get_project_history():

    history = []

    if not os.path.exists(OUTPUT_FOLDER):
        return history

    files = sorted(
        os.listdir(OUTPUT_FOLDER)
    )

    for file in files:

        if not file.endswith(".json"):
            continue

        path = os.path.join(
            OUTPUT_FOLDER,
            file
        )

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        history.append(
            {
                "file": file,
                "project_name": data.get(
                    "project_name",
                    "Untitled"
                ),
                "epics": len(
                    data.get("epics", [])
                )
            }
        )

    return history