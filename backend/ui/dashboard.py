import streamlit as st
from backend.storage.latest_project import (
    load_latest_project
)

from backend.utils.backlog_metrics import (
    get_backlog_metrics
)
def show_dashboard():

    st.markdown(
        "<div class='page-title'>Overview</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='page-subtitle'>AI-generated backlog pipeline status across all projects</div>",
        unsafe_allow_html=True
    )
    project, _ = load_latest_project()

    if project is not None:

        epics, features, stories, tasks = get_backlog_metrics(project)

    else:

        epics = features = stories = tasks = 0

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Epics", epics)

    with c2:
        st.metric("Features", features)

    with c3:
        st.metric("Stories", stories)

    with c4:
        st.metric("Tasks", tasks)

    st.divider()

    st.subheader("Recent Projects")

    st.dataframe(
        [
            {
                "Project":"Banking Portal",
                "Status":"Generated",
                "Last Updated":"Today"
            },
            {
                "Project":"Healthcare Platform",
                "Status":"Reviewed",
                "Last Updated":"Yesterday"
            },
            {
                "Project":"ERP System",
                "Status":"Pending Approval",
                "Last Updated":"2 Days Ago"
            }
        ],
        use_container_width=True
    )