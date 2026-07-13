import streamlit as st


def render_list(title, items):

    if not items:
        return

    st.markdown(f"**{title}**")

    for item in items:
        st.markdown(f"- {item}")

    st.write("")


def render_backlog(data):

    st.subheader(data["project_name"])

    if data.get("project_description"):

        st.info(data["project_description"])

    st.divider()

    for epic in data["epics"]:

        with st.expander(
            f"Epic • {epic['title']}",
            expanded=True
        ):

            # --------------------------------------------------
            # EPIC DETAILS
            # --------------------------------------------------

            st.subheader(epic["title"])

            st.markdown("### Business Objective")
            st.write(epic["business_objective"])

            st.markdown("### Business Value")
            st.write(epic["business_value"])

            st.markdown("### Description")
            st.write(epic["description"])

            col1, col2 = st.columns(2)

            with col1:

                render_list(
                    "Scope",
                    epic["scope"]
                )

                render_list(
                    "Assumptions",
                    epic["assumptions"]
                )

                render_list(
                    "Dependencies",
                    epic["dependencies"]
                )

            with col2:

                render_list(
                    "Out of Scope",
                    epic["out_of_scope"]
                )

                render_list(
                    "Risks",
                    epic["risks"]
                )

                render_list(
                    "Acceptance Criteria",
                    epic["acceptance_criteria"]
                )

            st.divider()

            st.markdown("## User Stories")

            # --------------------------------------------------
            # STORIES
            # --------------------------------------------------

            for story in epic["stories"]:

                with st.expander(
                    story["title"]
                ):

                    st.markdown("### Description")

                    st.write(
                        story["description"]
                    )

                    st.markdown("### User Story")

                    st.markdown(
                        f"""
**As a:** {story["as_a"]}

**I want:** {story["i_want"]}

**So that:** {story["so_that"]}
"""
                    )

                    c1, c2 = st.columns(2)

                    with c1:

                        st.metric(
                            "Priority",
                            story["priority"]
                        )

                    with c2:

                        st.metric(
                            "Story Points",
                            story["story_points"]
                        )

                    render_list(

                        "Acceptance Criteria",

                        story["acceptance_criteria"]

                    )

                    st.markdown("### Tasks")

                    for task in story["tasks"]:

                        with st.container():

                            st.markdown(
                                f"#### {task['title']}"
                            )

                            st.write(
                                task["description"]
                            )

                            st.success(
                                f"Definition of Done: {task['definition_of_done']}"
                            )

                            st.divider()