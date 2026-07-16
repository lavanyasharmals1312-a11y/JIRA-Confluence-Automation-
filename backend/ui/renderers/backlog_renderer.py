import streamlit as st


def render_list(title, items):

    if not items:
        return

    st.markdown(f"### {title}")

    for item in items:
        st.markdown(f"- {item}")

    st.write("")


def render_backlog(data):

    st.subheader(
        data.get(
            "project_name",
            "Generated Project"
        )
    )

    if data.get("project_description"):

        st.info(
            data["project_description"]
        )

    st.divider()

    for epic in data.get("epics", []):

        with st.expander(

            f"Epic • {epic.get('title','Untitled Epic')}",

            expanded=True

        ):

            # -------------------------------------------------
            # BASIC DESCRIPTION
            # -------------------------------------------------

            if epic.get("description"):

                st.markdown("### Description")

                st.write(
                    epic["description"]
                )

            # -------------------------------------------------
            # NEW FIELDS (SAFE)
            # -------------------------------------------------

            if epic.get("business_objective"):

                st.markdown("### Business Objective")

                st.write(
                    epic["business_objective"]
                )

            if epic.get("business_value"):

                st.markdown("### Business Value")

                st.write(
                    epic["business_value"]
                )

            col1, col2 = st.columns(2)

            with col1:

                render_list(
                    "Scope",
                    epic.get("scope", [])
                )

                render_list(
                    "Assumptions",
                    epic.get("assumptions", [])
                )

                render_list(
                    "Dependencies",
                    epic.get("dependencies", [])
                )

            with col2:

                render_list(
                    "Out of Scope",
                    epic.get("out_of_scope", [])
                )

                render_list(
                    "Risks",
                    epic.get("risks", [])
                )

                render_list(
                    "Acceptance Criteria",
                    epic.get(
                        "acceptance_criteria",
                        []
                    )
                )

            st.divider()

            st.markdown("## Stories")

            for story in epic.get("stories", []):

                with st.expander(

                    story.get(
                        "title",
                        "Untitled Story"
                    )

                ):

                    if story.get("description"):

                        st.markdown(
                            "### Description"
                        )

                        st.write(
                            story["description"]
                        )

                    # -----------------------------------------

                    if story.get("as_a"):

                        st.markdown(
                            "### User Story"
                        )

                        st.markdown(

f"""
**As a:** {story.get("as_a","")}

**I want:** {story.get("i_want","")}

**So that:** {story.get("so_that","")}
"""

                        )

                    c1, c2 = st.columns(2)

                    with c1:

                        if "priority" in story:

                            st.metric(

                                "Priority",

                                story.get(

                                    "priority",

                                    "Medium"

                                )

                            )

                    with c2:

                        if "story_points" in story:

                            st.metric(

                                "Story Points",

                                story.get(

                                    "story_points",

                                    "-"

                                )

                            )

                    render_list(

                        "Acceptance Criteria",

                        story.get(

                            "acceptance_criteria",

                            []

                        )

                    )

                    st.markdown(
                        "### Tasks"
                    )

                    for task in story.get(

                        "tasks",

                        []

                    ):

                        with st.container():

                            st.markdown(

                                f"#### {task.get('title','Task')}"

                            )

                            if task.get(

                                "description"

                            ):

                                st.write(

                                    task["description"]

                                )

                            if task.get(

                                "definition_of_done"

                            ):

                                st.success(

                                    f"Definition of Done: {task['definition_of_done']}"

                                )

                            st.divider()