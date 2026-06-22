import streamlit as st


def render_backlog(data):

    for epic in data["epics"]:

        with st.expander(
            epic["title"],
            expanded=True
        ):

            for story in epic["stories"]:

                with st.expander(
                    story["title"]
                ):

                    for task in story["tasks"]:

                        st.write(
                            task["title"]
                        )