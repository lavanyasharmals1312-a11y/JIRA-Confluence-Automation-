import os


from pathlib import Path

OUTPUT_FOLDER = (
    Path(__file__).resolve().parents[1] / "outputs"
)


def next_project_number():

    if not os.path.exists(OUTPUT_FOLDER):
        return 1

    files = [
        f for f in os.listdir(OUTPUT_FOLDER)
        if f.startswith("project_")
    ]

    return len(files) + 1