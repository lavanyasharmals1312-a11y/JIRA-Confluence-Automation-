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

    </style>
    """, unsafe_allow_html=True)