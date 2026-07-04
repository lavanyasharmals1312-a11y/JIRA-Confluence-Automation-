import os
from pathlib import Path

from dotenv import load_dotenv


env_path = (
    Path(__file__).resolve().parents[2] / ".env"
)

load_dotenv(env_path)


def get_jira_credentials():

    return {

        "base_url": os.getenv(
            "JIRA_BASE_URL"
        ),

        "email": os.getenv(
            "JIRA_EMAIL"
        ),

        "api_token": os.getenv(
            "JIRA_API_TOKEN"
        ),

        "project_key": os.getenv(
            "JIRA_PROJECT_KEY"
        )

    }


def get_confluence_credentials():

    return {

        "base_url": os.getenv(
            "CONFLUENCE_BASE_URL"
        ),

        "email": os.getenv(
            "CONFLUENCE_EMAIL"
        ),

        "api_token": os.getenv(
            "CONFLUENCE_API_TOKEN"
        )

    }