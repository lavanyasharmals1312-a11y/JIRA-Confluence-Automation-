import streamlit as st


def show_jira():

    st.title("Jira Integration")

    st.text_input(
        "Jira URL"
    )

    st.text_input(
        "Project Key"
    )

    st.text_input(
        "API Token",
        type="password"
    )

    st.warning(
        "Connection Not Configured"
    )

    st.button(
        "Connect Jira"
    )