import json
from pathlib import Path
from datetime import datetime

OUTPUT_FOLDER = (
    Path(__file__).resolve().parents[1] / "outputs"
)


def get_project_history():

    history = []

    if not OUTPUT_FOLDER.exists():
        return history

    for file in sorted(
        OUTPUT_FOLDER.glob("project_*.json"),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    ):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        history.append(
            {
                "Project": data.get(
                    "project_name",
                    "Untitled Project"
                ),
                "Status": data.get(
                    "status",
                    "Generated"
                ),
                "Epics": len(
                    data.get("epics", [])
                ),
                "Last Updated": datetime.fromtimestamp(
                    file.stat().st_mtime
                ).strftime("%d %b %Y %H:%M")
            }
        )

    return history