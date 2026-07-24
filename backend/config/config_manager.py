import json
from pathlib import Path

CONFIG_FILE = Path("backend/config/user_config.json")


def load_config():
    """
    Load the saved integration configuration.
    """

    if CONFIG_FILE.exists():

        with open(
            CONFIG_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    return {
        "gemini_api_key": "",
        "jira_email": "",
        "jira_api_token": "",
        "jira_base_url": "",
        "jira_project_key": ""
    }


def save_config(config):
    """
    Save the integration configuration.
    """

    CONFIG_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        CONFIG_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            config,
            f,
            indent=4
        )