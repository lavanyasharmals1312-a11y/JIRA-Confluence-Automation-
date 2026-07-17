import streamlit as st
from pathlib import Path


def load_css():

    css_path = Path(__file__).parent / "style.css"

    if css_path.exists():

        with open(css_path) as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )