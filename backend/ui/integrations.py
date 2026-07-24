import json
from pathlib import Path

import streamlit as st

from backend.config.config_manager import (
    load_config,
    save_config
)

from backend.integrations.connection_tests import (
    test_gemini_connection,
    test_jira_connection
)
def show_integrations():

    st.title("Integrations")

    st.caption(
        "Configure your Gemini and Jira credentials."
    )

    config = load_config()

    st.subheader("Gemini")

    gemini_key = st.text_input(
        "Gemini API Key",
        value=config["gemini_api_key"],
        type="password"
    )
    if st.button(
    "Test Gemini Connection",
    use_container_width=True
    ):

        success, message = test_gemini_connection(
            gemini_key
        )

        if success:
            st.success(message)
        else:
            st.error(message)

    st.divider()

    st.subheader("Jira")

    jira_email = st.text_input(
        "Atlassian Email",
        value=config["jira_email"]
    )

    jira_token = st.text_input(
        "API Token",
        value=config["jira_api_token"],
        type="password"
    )

    jira_url = st.text_input(
        "Jira Base URL",
        value=config["jira_base_url"]
    )

    jira_project = st.text_input(
        "Project Key",
        value=config["jira_project_key"]
    )
    if st.button(
    "Test Jira Connection",
    use_container_width=True
    ):

        success, message = test_jira_connection(
            jira_email,
            jira_token,
            jira_url,
            jira_project
        )

        if success:
            st.success(message)
        else:
            st.error(message)

    st.divider()

    if st.button(
        "Save Configuration",
        type="primary",
        width="stretch"
    ):

        save_config({

            "gemini_api_key": gemini_key,

            "jira_email": jira_email,

            "jira_api_token": jira_token,

            "jira_base_url": jira_url,

            "jira_project_key": jira_project

        })

        st.success(
            "Configuration saved successfully."
        )