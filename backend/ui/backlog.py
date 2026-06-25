import streamlit as st

from backend.storage.latest_project import (
    load_latest_project
)

from backend.ui.renderers.backlog_renderer import (
    render_backlog
)


def show_backlog():

    st.title(
        "Backlog Review"
    )

    data = load_latest_project()

    if data is None:

        st.info(
            "No generated projects found."
        )

        return

    epics = len(
        data["epics"]
    )

    stories = sum(

        len(epic["stories"])

        for epic in data["epics"]

    )

    tasks = sum(

        len(story["tasks"])

        for epic in data["epics"]

        for story in epic["stories"]

    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Epics",
            epics
        )

    with c2:
        st.metric(
            "Stories",
            stories
        )

    with c3:
        st.metric(
            "Tasks",
            tasks
        )

    with c4:
        st.metric(
            "Status",
            "Generated"
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button(
            "Approve"
        )

    with col2:
        st.button(
            "Request Changes"
        )

    with col3:
        st.button(
            "Push to Jira"
        )

    st.divider()

    render_backlog(data)