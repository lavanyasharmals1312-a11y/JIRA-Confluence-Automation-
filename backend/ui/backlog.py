import json
import streamlit as st

from ui.renderers.backlog_renderer import (
    render_backlog
)


def show_backlog():

    st.title(
        "Backlog Review"
    )

    with open(
        "outputs/project_001.json"
    ) as file:

        data = json.load(file)

    render_backlog(data)