import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(env_path)


def get_value(key):

    if key in st.secrets:
        print(f"{key} loaded from Streamlit Secrets")
        return st.secrets[key]

    value = os.getenv(key)

    print(f"{key} loaded from .env -> {value}")

    return value


def get_jira_credentials():

    creds = {

        "base_url": get_value("JIRA_BASE_URL"),

        "email": get_value("JIRA_EMAIL"),

        "api_token": get_value("JIRA_API_TOKEN"),

        "project_key": get_value("JIRA_PROJECT_KEY")

    }

    print("FINAL JIRA CREDS:", creds)

    return creds


def get_confluence_credentials():

    return {

        "base_url": get_value("CONFLUENCE_BASE_URL"),

        "email": get_value("CONFLUENCE_EMAIL"),

        "api_token": get_value("CONFLUENCE_API_TOKEN")

    }