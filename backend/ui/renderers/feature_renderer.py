import streamlit as st

from backend.ui.renderers.helpers import (
    render_text,
    render_textarea,
    render_list,
    section_heading,
    divider
)

from backend.ui.renderers.story_renderer import (
    render_story
)


def render_feature(feature, index):

    with st.expander(

        f"{feature.get('feature_id','FEAT')} • {feature.get('title','Feature')}",

        expanded=False

    ):

        # --------------------------------------------------
        # FEATURE DETAILS
        # --------------------------------------------------

        section_heading("Feature Details")

        render_text(

            feature,

            "feature_id",

            "Feature ID",

            f"featureid_{index}"

        )

        render_text(

            feature,

            "title",

            "Feature Title",

            f"featuretitle_{index}"

        )

        render_textarea(

            feature,

            "description",

            "Description",

            f"featuredesc_{index}",

            height=140

        )

        divider()

        # --------------------------------------------------
        # FEATURE INFORMATION
        # --------------------------------------------------

        section_heading("Feature Information")

        c1, c2 = st.columns(2)

        with c1:

            render_text(

                feature,

                "feature_type",

                "Feature Type",

                f"featuretype_{index}"

            )

        with c2:

            render_text(

            feature,

            "owner",

            "Feature Owner",

            f"featureowner_{index}"

            )

        render_text(

            feature,

            "estimated_sprint",

            "Estimated Sprint",

            f"sprint_{index}"

        )

        divider()

        # --------------------------------------------------
        # REQUIREMENTS
        # --------------------------------------------------

        section_heading("Requirements")

        render_list(

            feature,

            "functional_requirements",

            "Functional Requirements",

            f"functional_{index}"

        )

        render_list(

            feature,

            "non_functional_requirements",

            "Non Functional Requirements",

            f"nonfunctional_{index}"

        )

        divider()

        # --------------------------------------------------
        # TECHNICAL DETAILS
        # --------------------------------------------------

        section_heading("Technical Details")

        render_list(

            feature,

            "technical_notes",

            "Technical Notes",

            f"technical_{index}"

        )

        render_list(

            feature,

            "dependencies",

            "Dependencies",

            f"dependency_{index}"

        )

        render_list(

            feature,

            "acceptance_criteria",

            "Acceptance Criteria",

            f"featureacceptance_{index}"

        )

        divider()

        # --------------------------------------------------
        # USER STORIES
        # --------------------------------------------------

        section_heading("User Stories")

        stories = feature.get(

            "user_stories",

            []

        )

        if len(stories) == 0:

            st.info(

                "No User Stories Generated"

            )

        else:

            for story_index, story in enumerate(

                stories

            ):

                render_story(

                    story,

                    f"{index}_{story_index}"

                )

        divider()