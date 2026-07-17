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

from backend.ui.renderers.project_renderer import (
    render_project
)

st.error("THIS IS THE NEW BACKLOG.PY")
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

    if "confirm_push" not in st.session_state:

        st.session_state.confirm_push = False

    # -------------------------------------------------
    # METRICS
    # -------------------------------------------------

    epics = len(

        project.get("epics", [])

    )

    features = sum(

        len(epic.get("features", []))

        for epic in project.get("epics", [])

    )

    stories = sum(

        len(feature.get("user_stories", []))

        for epic in project.get("epics", [])

        for feature in epic.get("features", [])

    )

    tasks = sum(

        len(story.get("tasks", []))

        for epic in project.get("epics", [])

        for feature in epic.get("features", [])

        for story in feature.get("user_stories", [])

    )

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
    # SAVE CHANGES
    # -------------------------------------------------

    if st.session_state.edit_mode:

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

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

        with c2:

            pdf_path = generate_pdf(project)

            with open(

                pdf_path,

                "rb"

            ) as pdf:

                st.download_button(

                    "Download PDF",

                    data=pdf,

                    file_name=pdf_path.name,

                    mime="application/pdf",

                    width="stretch"

                )

    st.divider()
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
Project : {project.get('project_name','Project')}

Epics : {epics}

Features : {features}

Stories : {stories}

Tasks : {tasks}
"""
        )

        if st.button(

            "Push to Jira",

            type="primary",

            width="stretch"

        ):

            st.session_state.confirm_push = True

            st.rerun()

    # -------------------------------------------------
    # CONFIRMATION
    # -------------------------------------------------

    if st.session_state.confirm_push:

        st.warning(

            "Are you sure you want to publish this backlog to Jira?"

        )

        c1, c2 = st.columns(2)

        with c1:

            if st.button(

                "Confirm",

                type="primary",

                width="stretch"

            ):

                from backend.services.jira_service import (
                    push_project
                )

                with st.spinner(

                    "Publishing backlog..."

                ):

                    result = push_project(
                        project
                    )

                st.success(
                    f"""
Backlog Published Successfully

Epics : {len(result['epics'])}

Stories : {len(result['stories'])}

Tasks : {len(result['subtasks'])}
"""
                )

                st.session_state.confirm_push = False

        with c2:

            if st.button(

                "Cancel",

                width="stretch"

            ):

                st.session_state.confirm_push = False

                st.rerun()

    st.divider()

    # -------------------------------------------------
    # GENERATE NEW BACKLOG
    # -------------------------------------------------

    if st.button(

        "Generate New Backlog",

        width="stretch"

    ):

        st.session_state.edit_mode = False

        st.session_state.approved = False

        st.session_state.confirm_push = False

        st.session_state.page = "Upload Document"

        st.rerun()