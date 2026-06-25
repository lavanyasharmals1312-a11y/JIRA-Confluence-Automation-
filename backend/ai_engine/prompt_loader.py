from pathlib import Path


PROMPT_FOLDER = (
    Path(__file__).resolve().parents[1] / "prompts"
)


def load_prompt(filename):

    path = PROMPT_FOLDER / filename

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()