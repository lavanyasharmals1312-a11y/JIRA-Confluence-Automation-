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

from backend.ui.styles import load_css
from backend.ui.dashboard import show_dashboard
from backend.ui.upload import show_upload
from backend.ui.project_history import show_project_history
from backend.ui.backlog import show_backlog
from backend.ui.settings import show_settings

# ---------------------------------------------------
# LOAD CUSTOM CSS
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

with st.sidebar:

    st.markdown(
        """
        <h2 style='margin-bottom:0;'>📋 RequirementsAI</h2>
        <p style='color:#64748B;margin-top:0;'>
        AI Requirements Intelligence Platform
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("### Workspace")

    if st.button("Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"

    if st.button("Upload Document", use_container_width=True):
        st.session_state.page = "Upload Document"

    if st.button("Project History", use_container_width=True):
        st.session_state.page = "Project History"

    if st.button("Backlog Review", use_container_width=True):
        st.session_state.page = "Backlog Review"

    st.divider()

    st.markdown("### System")

    if st.button("Settings", use_container_width=True):
        st.session_state.page = "Settings"

    st.divider()

    st.success(f"Current Page\n\n**{st.session_state.page}**")

    st.caption("Version 1.0.0")

# ---------------------------------------------------
# PAGE ROUTING
# ---------------------------------------------------

page = st.session_state.page

if page == "Dashboard":

    show_dashboard()

elif page == "Upload Document":

    show_upload()

elif page == "Project History":

    show_project_history()

elif page == "Backlog Review":

    show_backlog()

elif page == "Settings":

    show_settings()