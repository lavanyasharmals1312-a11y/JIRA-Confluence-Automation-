import streamlit as st

def show_project_history():

    st.title(
        "Project History"
    )

    st.dataframe(
        [
            {
                "Project":"Banking Portal",
                "Status":"Approved",
                "Date":"23 Jun 2026"
            },
            {
                "Project":"Healthcare Platform",
                "Status":"Generated",
                "Date":"22 Jun 2026"
            }
        ],
        use_container_width=True
    )