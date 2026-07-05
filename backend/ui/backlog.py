import streamlit as st

from backend.storage.latest_project import (
    load_latest_project
)

from backend.services.jira_service import (
    push_project
)

from backend.ui.renderers.backlog_renderer import (
    render_backlog
)


def show_backlog():

    st.title("Generated Backlog")

    st.caption(
        "Review the AI-generated backlog before publishing it to Jira."
    )

    data = load_latest_project()

    if data is None:

        st.info(
            "No generated projects found."
        )

        return

    # -------------------------------------------------
    # METRICS
    # -------------------------------------------------

    epics = len(
        data["epics"]
    )

    stories = sum(

        len(epic["stories"])

        for epic in data["epics"]

    )

    subtasks = sum(

        len(story["tasks"])

        for epic in data["epics"]

        for story in epic["stories"]

    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Epics", epics)

    with c2:
        st.metric("Stories", stories)

    with c3:
        st.metric("Subtasks", subtasks)

    with c4:
        st.metric("Status", "Ready")

    st.divider()

    render_backlog(data)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(

            "Generate New Backlog",

            width="stretch"

        ):

            st.session_state.page = "Upload Document"

            st.rerun()

    with col2:

        if st.button(

            "Push to Jira",

            type="primary",

            width="stretch"

        ):

            try:

                with st.spinner(

                    "Publishing backlog to Jira..."

                ):

                    result = push_project(data)

                st.success(
                    f"""
Backlog successfully published to Jira.

Epics Created: {len(result['epics'])}
Stories Created: {len(result['stories'])}
Subtasks Created: {len(result['subtasks'])}
"""
                )

            except Exception as e:

                st.error(
                    f"Failed to publish backlog.\n\n{e}"
                )