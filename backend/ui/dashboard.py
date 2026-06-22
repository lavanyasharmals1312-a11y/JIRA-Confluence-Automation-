import streamlit as st

def show_dashboard():

    st.title("AI Requirements Intelligence Platform")

    st.caption(
        "Transform requirement documents into structured Agile backlogs."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Projects",
            "12"
        )

    with col2:
        st.metric(
            "Backlogs",
            "27"
        )

    with col3:
        st.metric(
            "Requirements Processed",
            "84"
        )

    with col4:
        st.metric(
            "Integrations",
            "2"
        )

    st.divider()

    st.subheader("Recent Activity")

    st.dataframe(
        [
            {
                "Project": "Project Alpha",
                "Status": "Generated"
            },
            {
                "Project": "Project Beta",
                "Status": "Reviewed"
            },
            {
                "Project": "Project Gamma",
                "Status": "Pending Approval"
            }
        ],
        use_container_width=True
    )