import streamlit as st


def show_confluence():

    st.title("Confluence Integration")

    st.text_input(
        "Confluence URL"
    )

    st.text_input(
        "Space Key"
    )

    st.text_input(
        "API Token",
        type="password"
    )

    st.warning(
        "Connection Not Configured"
    )

    st.button(
        "Connect Confluence"
    )