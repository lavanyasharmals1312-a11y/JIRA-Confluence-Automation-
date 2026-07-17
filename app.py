import streamlit as st
import os
st.sidebar.write(os.path.abspath(__file__))
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="RequirementsAI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)
def load_css():
    with open("backend/ui/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()
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

with st.sidebar:
    st.markdown(
"""
<div style="
text-align:center;
padding:10px 0 20px 0;
">

<h1 style="
margin:0;
font-size:34px;
font-weight:800;
color:white;
">
RequirementsAI
</h1>

<p style="
margin:6px 0 0 0;
font-size:14px;
color:rgba(255,255,255,.85);
">
AI Requirements Intelligence Platform
</p>

</div>
""",
unsafe_allow_html=True,
)

    st.markdown("---")

    st.markdown(
        """
        <div style="
        font-size:13px;
        font-weight:700;
        letter-spacing:1px;
        color:rgba(255,255,255,.75);
        margin-bottom:10px;
        ">
        WORKSPACE
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"

    if st.button("Upload Document", use_container_width=True):
        st.session_state.page = "Upload Document"

    if st.button("Project History", use_container_width=True):
        st.session_state.page = "Project History"

    if st.button("Backlog Review", use_container_width=True):
        st.session_state.page = "Backlog Review"

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
        font-size:13px;
        font-weight:700;
        letter-spacing:1px;
        color:rgba(255,255,255,.75);
        margin-bottom:10px;
        ">
        SYSTEM
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Settings", use_container_width=True):
        st.session_state.page = "Settings"

    st.markdown("---")

    st.markdown(
        f"""
        <div style="
        background:rgba(255,255,255,.12);
        padding:16px;
        border-radius:14px;
        ">

        <div style="
        font-size:12px;
        color:rgba(255,255,255,.75);
        ">
        CURRENT PAGE
        </div>

        <div style="
        font-size:20px;
        font-weight:700;
        margin-top:6px;
        color:white;
        ">
        {st.session_state.page}
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div style="
        text-align:center;
        font-size:12px;
        color:rgba(255,255,255,.65);
        ">

        Version 1.0.0

        </div>
        """,
        unsafe_allow_html=True,
    )

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