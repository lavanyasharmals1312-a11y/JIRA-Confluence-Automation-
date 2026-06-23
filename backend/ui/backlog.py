import json
import os
import streamlit as st

from ui.renderers.backlog_renderer import render_backlog


def show_backlog():

    st.title("Backlog Review")

    current_dir = os.path.dirname(__file__)

    json_path = os.path.join(
        current_dir,
        "..",
        "outputs",
        "project_001.json"
    )

    json_path = os.path.abspath(json_path)

    with open(json_path, "r") as file:
        data = json.load(file)

    render_backlog(data)