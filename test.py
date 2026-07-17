import streamlit as st

st.set_page_config(layout="wide")

with st.sidebar:
    st.markdown(
        """
        <div style="background:red;color:white;padding:20px;border-radius:10px;">
            <h2>RequirementsAI</h2>
            <p>Hello World</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("Hello")