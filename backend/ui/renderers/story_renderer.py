import streamlit as st

from backend.ui.renderers.helpers import (
    render_text,
    render_textarea,
    render_list,
    render_number,
    section_heading,
    divider
)

from backend.ui.renderers.task_renderer import (
    render_task
)


def render_story(story, index):

    with st.expander(

        f"{story.get('story_id','US')} • {story.get('title','User Story')}",

        expanded=False

    ):

        # --------------------------------------------------
        # STORY DETAILS
        # --------------------------------------------------

        section_heading("User Story")

        render_text(

            story,

            "story_id",

            "Story ID",

            f"storyid_{index}"

        )

        render_text(

            story,

            "title",

            "Story Title",

            f"storytitle_{index}"

        )

        render_textarea(

            story,

            "detailed_description",

            "Description",

            f"storydesc_{index}",

            height=140

        )

        divider()

        # --------------------------------------------------
        # USER STORY FORMAT
        # --------------------------------------------------

        section_heading("Business Requirement")

        render_text(

            story,

            "as_a",

            "As a",

            f"asa_{index}"

        )

        render_text(

            story,

            "i_want",

            "I want",

            f"iwant_{index}"

        )

        render_text(

            story,

            "so_that",

            "So that",

            f"sothat_{index}"

        )

        divider()

        # --------------------------------------------------
        # BUSINESS RULES
        # --------------------------------------------------

        section_heading("Business Rules")

        render_list(

            story,

            "business_rules",

            "Business Rules",

            f"rules_{index}"

        )

        render_list(

            story,

            "preconditions",

            "Preconditions",

            f"pre_{index}"

        )

        render_list(

            story,

            "postconditions",

            "Postconditions",

            f"post_{index}"

        )

        divider()

        # --------------------------------------------------
        # STORY METADATA
        # --------------------------------------------------

        section_heading("Planning")

        c1, c2 = st.columns(2)

        with c1:

            render_text(

                story,

                "priority",

                "Priority",

                f"priority_{index}"

            )

            render_text(

                story,

                "estimated_effort",

                "Estimated Effort",

                f"effort_{index}"

            )

        with c2:

            render_number(

                story,

                "story_points",

                "Story Points",

                f"points_{index}"

            )

            render_text(

                story,

                "assigned_team",

                "Assigned Team",

                f"team_{index}"

            )

        divider()

        # --------------------------------------------------
        # LABELS & ACCEPTANCE
        # --------------------------------------------------

        section_heading("Quality")

        render_list(

            story,

            "labels",

            "Labels",

            f"labels_{index}"

        )

        render_list(

            story,

            "acceptance_criteria",

            "Acceptance Criteria",

            f"acceptance_{index}"

        )

        divider()

        # --------------------------------------------------
        # TASKS
        # --------------------------------------------------

        section_heading("Implementation Tasks")

        tasks = story.get(

            "tasks",

            []

        )

        if len(tasks) == 0:

            st.info(

                "No Tasks Generated"

            )

        else:

            for task_index, task in enumerate(

                tasks

            ):

                render_task(

                    task,

                    f"{index}_{task_index}"

                )

        divider()