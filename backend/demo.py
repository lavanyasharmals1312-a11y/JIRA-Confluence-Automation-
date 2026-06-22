import streamlit as st

from ui.dashboard import show_dashboard
from ui.upload import show_upload
from ui.backlog import show_backlog
from ui.jira import show_jira
from ui.confluence import show_confluence
from ui.settings import show_settings

st.set_page_config(
    page_title="AI Requirements Intelligence Platform",
    layout="wide"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Requirement Ingestion",
        "Backlog Review",
        "Jira Integration",
        "Confluence Integration",
        "Settings"
    ]
)

if page == "Dashboard":
    show_dashboard()

elif page == "Requirement Ingestion":
    show_upload()

elif page == "Backlog Review":
    show_backlog()

elif page == "Jira Integration":
    show_jira()

elif page == "Confluence Integration":
    show_confluence()

elif page == "Settings":
    show_settings()