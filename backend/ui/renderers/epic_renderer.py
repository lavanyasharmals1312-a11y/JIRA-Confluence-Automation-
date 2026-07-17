import streamlit as st

from backend.ui.renderers.helpers import (
    render_text,
    render_textarea,
    render_list,
    section_heading,
    divider
)

from backend.ui.renderers.feature_renderer import (
    render_feature
)


def render_epic(epic, index):

    with st.expander(

        f"{epic.get('epic_id','EP')} • {epic.get('title','Epic')}",

        expanded=True

    ):

        # --------------------------------------------------
        # BASIC INFORMATION
        # --------------------------------------------------

        section_heading("Epic Details")

        render_text(

            epic,

            "epic_id",

            "Epic ID",

            f"epicid_{index}"

        )

        render_text(

            epic,

            "title",

            "Epic Title",

            f"epictitle_{index}"

        )

        render_textarea(

            epic,

            "description",

            "Description",

            f"epicdesc_{index}",

            height=150

        )

        divider()

        # --------------------------------------------------
        # BUSINESS DETAILS
        # --------------------------------------------------

        section_heading("Business Information")

        render_textarea(

            epic,

            "business_objective",

            "Business Objective",

            f"objective_{index}",

            height=120

        )

        render_textarea(

            epic,

            "business_value",

            "Business Value",

            f"value_{index}",

            height=120

        )

        divider()

        # --------------------------------------------------
        # SCOPE
        # --------------------------------------------------

        section_heading("Scope")

        render_list(

            epic,

            "scope",

            "Scope",

            f"scope_{index}"

        )

        render_list(

            epic,

            "out_of_scope",

            "Out of Scope",

            f"outscope_{index}"

        )

        divider()

        # --------------------------------------------------
        # PLANNING
        # --------------------------------------------------

        section_heading("Planning")

        render_list(

            epic,

            "assumptions",

            "Assumptions",

            f"assumption_{index}"

        )

        render_list(

            epic,

            "dependencies",

            "Dependencies",

            f"dependency_{index}"

        )

        render_list(

            epic,

            "risks",

            "Risks",

            f"risk_{index}"

        )

        render_list(

            epic,

            "success_metrics",

            "Success Metrics",

            f"success_{index}"

        )

        divider()

        # --------------------------------------------------
        # FEATURES
        # --------------------------------------------------

        section_heading("Features")

        features = epic.get(

            "features",

            []

        )

        if len(features) == 0:

            st.info(

                "No Features Generated"

            )

        else:

            for feature_index, feature in enumerate(

                features

            ):

                render_feature(

                    feature,

                    f"{index}_{feature_index}"

                )

