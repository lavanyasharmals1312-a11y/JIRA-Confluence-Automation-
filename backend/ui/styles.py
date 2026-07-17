import streamlit as st

def load_css():

    st.markdown("""
    <style>

    .main {
        background-color: #F7F8FA;
    }

    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }

    .section-card {
        background: white;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #E5E7EB;
        margin-bottom: 16px;
    }

    .page-title {
        font-size: 28px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .page-subtitle {
        color: #6B7280;
        font-size: 14px;
        margin-bottom: 24px;
    }

    /* ---------------------------------------------------
       SIDEBAR - dark theme
       The sidebar HTML in app.py uses white/light text
       (rgba(255,255,255,...)), which needs a dark
       background behind it to actually be visible.
    --------------------------------------------------- */

    [data-testid="stSidebar"] {
    background: #111827 !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        background: #111827 !important;
    }

    /* Native Streamlit buttons (Dashboard, Upload, etc.) */
    [data-testid="stSidebar"] .stButton > button {
        background-color: rgba(255,255,255,.06);
        color: #FFFFFF;
        border: 1px solid rgba(255,255,255,.15);
        border-radius: 8px;
        width: 100%;
        text-align: left;
        padding: 10px 14px;
        font-weight: 500;
        transition: background-color 0.15s ease;
    }

    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: rgba(255,255,255,.16);
        border-color: rgba(255,255,255,.3);
        color: #FFFFFF;
    }

    [data-testid="stSidebar"] .stButton > button:focus:not(:active) {
        color: #FFFFFF;
        border-color: rgba(255,255,255,.3);
    }

    /* "---" dividers rendered as <hr> inside the sidebar */
    [data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,.15);
    }

    </style>
    """, unsafe_allow_html=True)