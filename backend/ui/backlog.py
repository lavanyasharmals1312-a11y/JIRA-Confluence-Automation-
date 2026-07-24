import streamlit as st

from backend.storage.latest_project import (
    load_latest_project
)

from backend.storage.save_project import (
    save_existing_project
)

from backend.services.pdf_service import (
    generate_pdf
)
from backend.utils.backlog_metrics import (
    get_backlog_metrics
)
from backend.ui.renderers.project_renderer import (
    render_project
)
@st.dialog("Confirm Publish")
def confirm_publish_dialog(project):

    st.write(
        "Are you sure you want to publish this backlog to Jira?"
    )

    c1, c2 = st.columns(2)

    with c1:

        if st.button("Publish", type="primary"):

            from backend.services.jira_service import push_project

            with st.spinner("Publishing backlog..."):

                result = push_project(project)

            st.success(
                f"""
Backlog Published Successfully

Epics : {len(result['epics'])}
Features : {len(result['features'])}
Stories : {len(result['stories'])}
Tasks : {len(result['tasks'])}
"""
            )

            st.rerun()

    with c2:

        if st.button("Cancel"):

            st.rerun()

def show_backlog():

    st.title("Backlog Review")

    st.caption(
        "Review the generated backlog before publishing it to Jira."
    )

    project, filepath = load_latest_project()

    if project is None:

        st.info(
            "No generated backlog found."
        )

        return

    # -------------------------------------------------
    # SESSION STATE
    # -------------------------------------------------

    if "edit_mode" not in st.session_state:

        st.session_state.edit_mode = False

    if "approved" not in st.session_state:

        st.session_state.approved = False

    # -------------------------------------------------
    # METRICS
    # -------------------------------------------------

    epics, features, stories, tasks = get_backlog_metrics(project)
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

    # -------------------------------------------------
    # RENDER PROJECT
    # -------------------------------------------------
    st.info(
    "Expand each Epic to reveal its Features, User Stories, and Tasks."
    )
    render_project(project)

    st.divider()

    # -------------------------------------------------
    # REVIEW ACTIONS
    # -------------------------------------------------

    st.subheader("Review Actions")

    col1, col2 = st.columns(2)

    with col1:

        if not st.session_state.edit_mode:

            if st.button(

                "Modify",

                width="stretch"

            ):

                st.session_state.edit_mode = True

                st.rerun()

    with col2:

        if not st.session_state.approved:

            if st.button(

                "Approve",

                type="primary",

                width="stretch"

            ):

                st.session_state.approved = True

                st.success(

                    "Backlog approved successfully."

                )

                st.rerun()


    # -------------------------------------------------
    # DOWNLOAD PDF
    # -------------------------------------------------

    st.divider()

    pdf_path = generate_pdf(project)

    with open(pdf_path, "rb") as pdf:

        st.download_button(

            "Download PDF",

            data=pdf,

            file_name=pdf_path.name,

            mime="application/pdf",

            width="stretch"

        )

    # -------------------------------------------------
    # SAVE CHANGES
    # -------------------------------------------------

    if st.session_state.edit_mode:

        st.divider()

        if st.button(

            "Save Changes",

            type="primary",

            width="stretch"

        ):

            save_existing_project(

                project,

                filepath

            )

            st.success(

                "Changes saved successfully."

            )

            st.session_state.edit_mode = False

            st.rerun()
    # -------------------------------------------------
    # APPROVED
    # -------------------------------------------------

    if st.session_state.approved:

        st.success(
            "Project Manager Approval Received"
        )

        st.subheader(
            "Publish Backlog"
        )

        st.info(
            f"""
Project : {project.get('project_name', 'Project')}

Epics : {epics}

Features : {features}

Stories : {stories}

Tasks : {tasks}
"""
        )

        st.subheader("Select Epics to Publish")

        selected_epics = []

        for epic in project.get("epics", []):

            if st.checkbox(
                epic.get("title", "Untitled Epic"),
                value=True,
                key=f"epic_{epic.get('title')}"
            ):

                selected_epics.append(epic)

        filtered_project = {
            **project,
            "epics": selected_epics
        }

        if st.button(
            "Push to Jira",
            type="primary",
            width="stretch"
        ):

            if not selected_epics:

                st.error(
                    "Please select at least one Epic to publish."
                )

            else:

                confirm_publish_dialog(filtered_project)
    # -------------------------------------------------
    # GENERATE NEW BACKLOG
    # -------------------------------------------------

    if st.button(

        "Generate New Backlog",

        width="stretch"

    ):

        st.session_state.edit_mode = False

        st.session_state.approved = False

        st.session_state.page = "Upload Document"

        st.rerun()