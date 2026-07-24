import os
from pathlib import Path

from dotenv import load_dotenv
from backend.config.config_manager import load_config

# Load .env
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

# Streamlit is optional
try:
    import streamlit as st
except ImportError:
    st = None


def get_value(key):
    """
    Reads a value from:
    1. .env
    2. Streamlit Secrets (only if running inside Streamlit)

    .env is preferred for local development.
    """

    # First check .env
    value = os.getenv(key)

    if value:
        print(f"{key} loaded from .env")
        return value

    # Then check Streamlit Secrets
    if st is not None:
        try:
            if key in st.secrets:
                print(f"{key} loaded from Streamlit Secrets")
                return st.secrets[key]
        except Exception:
            # Not running inside Streamlit
            pass

    raise ValueError(f"Missing configuration value: {key}")


def get_jira_credentials():

    config = load_config()

    return {

        "base_url":
            config.get("jira_base_url")
            or get_value("JIRA_BASE_URL"),

        "email":
            config.get("jira_email")
            or get_value("JIRA_EMAIL"),

        "api_token":
            config.get("jira_api_token")
            or get_value("JIRA_API_TOKEN"),

        "project_key":
            config.get("jira_project_key")
            or get_value("JIRA_PROJECT_KEY")

    }


def get_confluence_credentials():

    return {
        "base_url": get_value("CONFLUENCE_BASE_URL"),
        "email": get_value("CONFLUENCE_EMAIL"),
        "api_token": get_value("CONFLUENCE_API_TOKEN")
    }