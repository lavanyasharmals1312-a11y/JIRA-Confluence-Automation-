import json
import os
import streamlit as st

from ui.renderers.backlog_renderer import render_backlog
c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric("Epics",4)

with c2:
    st.metric("Stories",11)

with c3:
    st.metric("Tasks",34)

with c4:
    st.metric("Status","Generated")

col1,col2,col3 = st.columns(3)

with col1:
    st.button("Approve")

with col2:
    st.button("Request Changes")

with col3:
    st.button("Push To Jira")

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