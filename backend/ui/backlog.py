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


def show_backlog():

    # =====================================================
    # PAGE HEADER
    # =====================================================

    st.markdown(
        """
        <div style="
            background:linear-gradient(135deg,#2563EB,#4F46E5);
            padding:32px;
            border-radius:20px;
            color:white;
            margin-bottom:28px;
            box-shadow:0 10px 28px rgba(37,99,235,.22);
        ">

            <div style="
                font-size:34px;
                font-weight:800;
                margin-bottom:8px;
            ">
                Backlog Review
            </div>

            <div style="
                font-size:17px;
                opacity:.92;
            ">
                Review, edit and approve the generated backlog before publishing it to Jira.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    project, filepath = load_latest_project()

    if project is None:

        st.info("No generated backlog found.")

        return

    # =====================================================
    # SESSION STATE
    # =====================================================

    if "edit_mode" not in st.session_state:
        st.session_state.edit_mode = False

    if "approved" not in st.session_state:
        st.session_state.approved = False

    if "confirm_push" not in st.session_state:
        st.session_state.confirm_push = False

    # =====================================================
    # METRICS
    # =====================================================

    epics = len(project.get("epics", []))

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

    # =====================================================
    # PROJECT OVERVIEW
    # =====================================================

    left, right = st.columns([3, 1], gap="large")

    with left:

        st.markdown("## Project Overview")

        st.markdown(
            f"""
            <div style="
                background:white;
                border:1px solid #E5E7EB;
                border-radius:18px;
                padding:24px;
                box-shadow:0 6px 20px rgba(0,0,0,.05);
            ">

                <table style="width:100%;font-size:15px;">

                    <tr>
                        <td width="35%"><b>Project Name</b></td>
                        <td>{project.get("project_name","Untitled Project")}</td>
                    </tr>

                    <tr>
                        <td><b>Status</b></td>
                        <td>
                            {"Approved" if st.session_state.approved else "Pending Review"}
                        </td>
                    </tr>

                    <tr>
                        <td><b>Edit Mode</b></td>
                        <td>
                            {"Enabled" if st.session_state.edit_mode else "Disabled"}
                        </td>
                    </tr>

                </table>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:

        st.markdown("## Actions")

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                border:1px solid #E5E7EB;
                padding:22px;
                box-shadow:0 6px 20px rgba(0,0,0,.05);
            ">

                <div style="
                    font-size:18px;
                    font-weight:700;
                    margin-bottom:14px;
                ">
                    Review Checklist
                </div>

                <div style="line-height:2;">

                    • Validate Epics<br>

                    • Verify Features<br>

                    • Review User Stories<br>

                    • Check Task Breakdown<br>

                    • Approve for Publishing

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # KPI CARDS
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Epics", epics)

    with c2:
        st.metric("Features", features)

    with c3:
        st.metric("User Stories", stories)

    with c4:
        st.metric("Tasks", tasks)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # BACKLOG
    # =====================================================
    # =====================================================
    # PROJECT STRUCTURE
    # =====================================================

    st.markdown("## Project Structure")

    st.markdown(
        """
        <div style="
            background:white;
            border:1px solid #E5E7EB;
            border-radius:18px;
            padding:18px;
            margin-bottom:24px;
            box-shadow:0 6px 20px rgba(0,0,0,.05);
        ">
            Review the generated project hierarchy. Expand individual sections to inspect
            Epics, Features, User Stories and Tasks before approving the backlog.
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_project(project)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # REVIEW ACTIONS
    # =====================================================

    st.markdown("## Review Actions")

    action_left, action_right = st.columns([2, 1], gap="large")

    with action_left:

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                border:1px solid #E5E7EB;
                padding:24px;
                box-shadow:0 6px 20px rgba(0,0,0,.05);
            ">

                <div style="
                    font-size:22px;
                    font-weight:700;
                    margin-bottom:10px;
                    color:#0F172A;
                ">
                    Review Status
                </div>

                <div style="
                    color:#64748B;
                    line-height:1.9;
                ">

                    • Validate project hierarchy<br>

                    • Review acceptance criteria<br>

                    • Verify task decomposition<br>

                    • Save any required modifications<br>

                    • Approve backlog for publishing

                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with action_right:

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                border:1px solid #E5E7EB;
                padding:24px;
                box-shadow:0 6px 20px rgba(0,0,0,.05);
                margin-bottom:20px;
            ">
                <div style="
                    font-size:18px;
                    font-weight:700;
                    margin-bottom:8px;
                ">
                    Current Status
                </div>
            """,
            unsafe_allow_html=True,
        )

        if st.session_state.approved:

            st.success("Approved")

        elif st.session_state.edit_mode:

            st.warning("Editing")

        else:

            st.info("Pending Review")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # PRIMARY ACTIONS
    # =====================================================

    c1, c2 = st.columns(2)

    with c1:

        if not st.session_state.edit_mode:

            if st.button(
                "Modify Backlog",
                use_container_width=True
            ):

                st.session_state.edit_mode = True

                st.rerun()

    with c2:

        if not st.session_state.approved:

            if st.button(
                "Approve Backlog",
                use_container_width=True,
                type="primary"
            ):

                st.session_state.approved = True

                st.success(
                    "Backlog approved successfully."
                )

                st.rerun()

    # =====================================================
    # SAVE PANEL
    # =====================================================

    if st.session_state.edit_mode:

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("## Save Changes")

        st.markdown(
            """
            <div style="
                background:white;
                border-radius:18px;
                border:1px solid #E5E7EB;
                padding:22px;
                margin-bottom:18px;
                box-shadow:0 6px 20px rgba(0,0,0,.05);
            ">
                Save your modifications before publishing the project backlog.
            </div>
            """,
            unsafe_allow_html=True,
        )

        c1, c2 = st.columns(2)

        with c1:

            if st.button(
                "Save Changes",
                use_container_width=True,
                type="primary"
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

            with open(pdf_path, "rb") as pdf:

                st.download_button(
                    "Download PDF",
                    data=pdf,
                    file_name=pdf_path.name,
                    mime="application/pdf",
                    use_container_width=True
                )

    st.markdown("<br>", unsafe_allow_html=True)
    # =====================================================
    # APPROVAL & PUBLISH
    # =====================================================

    if st.session_state.approved:

        st.markdown("## Publish Backlog")

        left, right = st.columns([2, 1], gap="large")

        with left:

            st.markdown(
                f"""
                <div style="
                    background:white;
                    border-radius:18px;
                    border:1px solid #E5E7EB;
                    padding:24px;
                    box-shadow:0 6px 20px rgba(0,0,0,.05);
                ">

                <div style="
                    font-size:22px;
                    font-weight:700;
                    margin-bottom:18px;
                    color:#0F172A;
                ">
                    Project Ready for Publishing
                </div>

                <table style="width:100%;font-size:15px;">

                    <tr>
                        <td width="40%"><b>Project</b></td>
                        <td>{project.get("project_name","Project")}</td>
                    </tr>

                    <tr>
                        <td><b>Epics</b></td>
                        <td>{epics}</td>
                    </tr>

                    <tr>
                        <td><b>Features</b></td>
                        <td>{features}</td>
                    </tr>

                    <tr>
                        <td><b>User Stories</b></td>
                        <td>{stories}</td>
                    </tr>

                    <tr>
                        <td><b>Tasks</b></td>
                        <td>{tasks}</td>
                    </tr>

                </table>

                </div>
                """,
                unsafe_allow_html=True,
            )

        with right:

            st.markdown(
                """
                <div style="
                    background:white;
                    border-radius:18px;
                    border:1px solid #E5E7EB;
                    padding:24px;
                    box-shadow:0 6px 20px rgba(0,0,0,.05);
                ">

                <div style="
                    font-size:18px;
                    font-weight:700;
                    margin-bottom:12px;
                ">
                    Publishing Status
                </div>

                Ready for Jira

                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button(
                "Publish to Jira",
                use_container_width=True,
                type="primary"
            ):

                st.session_state.confirm_push = True

                st.rerun()

    # =====================================================
    # CONFIRMATION
    # =====================================================

    if st.session_state.confirm_push:

        st.warning(
            "Confirm publishing this backlog to Jira?"
        )

        c1, c2 = st.columns(2)

        with c1:

            if st.button(
                "Confirm Publish",
                use_container_width=True,
                type="primary"
            ):

                from backend.services.jira_service import (
                    push_project
                )

                with st.spinner(
                    "Publishing backlog..."
                ):

                    result = push_project(project)

                st.success(
                    f"""
                Publishing completed successfully.

                Epics Created: {len(result['epics'])}

                Stories Created: {len(result['stories'])}

                Tasks Created: {len(result['subtasks'])}
                """
                )

                st.session_state.confirm_push = False

        with c2:

            if st.button(
                "Cancel",
                use_container_width=True
            ):

                st.session_state.confirm_push = False

                st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # NEW PROJECT
    # =====================================================

    st.markdown(
        """
        <div style="
            background:white;
            border-radius:18px;
            border:1px solid #E5E7EB;
            padding:22px;
            text-align:center;
            box-shadow:0 6px 20px rgba(0,0,0,.05);
        ">

            <div style="
                font-size:22px;
                font-weight:700;
                margin-bottom:8px;
            ">
                Start Another Project
            </div>

            <div style="
                color:#64748B;
            ">
                Return to the upload page and generate a new backlog.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "Generate New Backlog",
        use_container_width=True
    ):

        st.session_state.edit_mode = False
        st.session_state.approved = False
        st.session_state.confirm_push = False

        st.session_state.page = "Upload Document"

        st.rerun()