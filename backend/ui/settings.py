import streamlit as st


def show_settings():

    st.title("Platform Settings")

    st.selectbox(
        "AI Provider",
        [
            "Gemini",
            "Azure OpenAI",
            "Claude"
        ]
    )

    st.selectbox(
        "Output Format",
        [
            "JSON",
            "Jira Ready JSON"
        ]
    )

    st.button(
        "Save Settings"
    )