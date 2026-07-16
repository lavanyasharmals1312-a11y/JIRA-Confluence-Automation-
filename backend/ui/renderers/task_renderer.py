import streamlit as st

from backend.ui.renderers.helpers import (
    render_text,
    render_textarea,
    render_number,
    section_heading,
    divider
)


def render_task(task, index):

    with st.expander(

        f"{task.get('task_id','TASK')} • {task.get('title','Task')}",

        expanded=False

    ):

        # --------------------------------------------------
        # TASK DETAILS
        # --------------------------------------------------

        section_heading("Task Details")

        render_text(

            task,

            "task_id",

            "Task ID",

            f"taskid_{index}"

        )

        render_text(

            task,

            "title",

            "Task Title",

            f"tasktitle_{index}"

        )

        render_textarea(

            task,

            "description",

            "Description",

            f"taskdesc_{index}",

            height=130

        )

        divider()

        # --------------------------------------------------
        # IMPLEMENTATION DETAILS
        # --------------------------------------------------

        section_heading("Implementation")

        col1, col2 = st.columns(2)

        with col1:

            render_text(

                task,

                "task_type",

                "Task Type",

                f"tasktype_{index}"

            )

        with col2:

            render_number(

                task,

                "estimated_hours",

                "Estimated Hours",

                f"hours_{index}"

            )

        divider()

        # --------------------------------------------------
        # DEFINITION OF DONE
        # --------------------------------------------------

        section_heading("Definition of Done")

        render_textarea(

            task,

            "definition_of_done",

            "Definition of Done",

            f"dod_{index}",

            height=120

        )

        divider()