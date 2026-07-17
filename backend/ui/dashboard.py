import streamlit as st

def show_dashboard():

    st.markdown(
        "<div class='page-title'>Overview</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='page-subtitle'>AI-generated backlog pipeline status across all projects</div>",
        unsafe_allow_html=True
    )

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.metric(
            "Projects",
            "12",
            "+3"
        )

    with c2:
        st.metric(
            "Backlogs Generated",
            "27",
            "+5"
        )

    with c3:
        st.metric(
            "Requirements Processed",
            "84",
            "+12"
        )

    with c4:
        st.metric(
            "Integrations",
            "2"
        )

    st.divider()

    st.subheader("Recent Projects")

    st.dataframe(
        [
            {
                "Project":"Banking Portal",
                "Status":"Generated",
                "Last Updated":"Today"
            },
            {
                "Project":"Healthcare Platform",
                "Status":"Reviewed",
                "Last Updated":"Yesterday"
            },
            {
                "Project":"ERP System",
                "Status":"Pending Approval",
                "Last Updated":"2 Days Ago"
            }
        ],
        use_container_width=True
    )