import streamlit as st

from backend.storage.project_history import (
    get_project_history
)


def show_project_history():

    st.title("Project History")

    history = get_project_history()

    if not history:
        st.info("No projects have been generated yet.")
        return

    st.dataframe(
        history,
        hide_index=True,
        width="stretch"
    )