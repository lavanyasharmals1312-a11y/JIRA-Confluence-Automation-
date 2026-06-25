import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Requirements Intelligence Platform",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# IMPORTS
# -----------------------------

from ui.styles import load_css

from ui.dashboard import show_dashboard
from ui.upload import show_upload
from ui.project_history import show_project_history
from ui.backlog import show_backlog
from ui.jira import show_jira
from ui.confluence import show_confluence
from ui.settings import show_settings

# -----------------------------
# LOAD GLOBAL CSS
# -----------------------------

load_css()

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("RequirementsAI")

st.sidebar.caption(
    "AI Requirements Intelligence Platform"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Requirement Ingestion",
        "Project History",
        "Backlog Review",
        "Jira Integration",
        "Confluence Integration",
        "Settings"
    ]
)

st.sidebar.divider()

st.sidebar.caption("Version 1.0.0")
# -----------------------------
# PAGE ROUTING
# -----------------------------

page = workspace_page

if integration_page:
    if st.session_state.integration != "":
        page = integration_page

if system_page:
    if st.session_state.system != "":
        page = system_page

# -----------------------------
# RENDER PAGE
# -----------------------------

if page == "Dashboard":

    show_dashboard()

elif page == "Requirement Ingestion":

    show_upload()

elif page == "Project History":

    show_project_history()

elif page == "Backlog Review":

    show_backlog()

elif page == "Jira Integration":

    show_jira()

elif page == "Confluence Integration":

    show_confluence()

elif page == "Settings":

    show_settings()