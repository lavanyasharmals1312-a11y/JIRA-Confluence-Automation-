import streamlit as st
from backend.storage.latest_project import (
    load_latest_project
)
from backend.storage.project_history import (
    get_project_history
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

    history = get_project_history()

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )