import streamlit as st

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Requirements Intelligence Platform",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# IMPORTS
# ---------------------------------------------------

from ui.styles import load_css
from ui.dashboard import show_dashboard
from ui.upload import show_upload
from ui.project_history import show_project_history
from ui.backlog import show_backlog
from ui.jira import show_jira
from ui.confluence import show_confluence
from ui.settings import show_settings

# ---------------------------------------------------
# LOAD CSS
# ---------------------------------------------------

load_css()

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("RequirementsAI")
st.sidebar.caption("AI Requirements Intelligence Platform")

st.sidebar.divider()

st.sidebar.markdown("### Workspace")

if st.sidebar.button("Dashboard", use_container_width=True):
    st.session_state.page = "Dashboard"

if st.sidebar.button("Requirement Ingestion", use_container_width=True):
    st.session_state.page = "Requirement Ingestion"

if st.sidebar.button("Project History", use_container_width=True):
    st.session_state.page = "Project History"

if st.sidebar.button("Backlog Review", use_container_width=True):
    st.session_state.page = "Backlog Review"

st.sidebar.divider()

st.sidebar.markdown("### Integrations")

if st.sidebar.button("Jira Integration", use_container_width=True):
    st.session_state.page = "Jira Integration"

if st.sidebar.button("Confluence Integration", use_container_width=True):
    st.session_state.page = "Confluence Integration"

st.sidebar.divider()

st.sidebar.markdown("### System")

if st.sidebar.button("⚙ Settings", use_container_width=True):
    st.session_state.page = "Settings"

st.sidebar.divider()

st.sidebar.markdown(
    f"**Current Page**  \n{st.session_state.page}"
)

st.sidebar.caption("Version 1.0.0")

# ---------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------

page = st.session_state.page

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