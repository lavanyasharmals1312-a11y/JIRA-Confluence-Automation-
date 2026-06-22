import streamlit as st


def show_backlog():

    st.title("Backlog Review")

    with st.expander(
        "User Management",
        expanded=True
    ):

        with st.expander(
            "User Registration"
        ):

            st.write(
                "Design Registration Screen"
            )

            st.write(
                "Create Registration API"
            )

            st.write(
                "Validation Rules"
            )

        with st.expander(
            "Authentication"
        ):

            st.write(
                "Login Service"
            )

            st.write(
                "Password Reset"
            )

    with st.expander(
        "Reporting & Analytics"
    ):

        with st.expander(
            "Dashboard Reports"
        ):

            st.write(
                "Analytics Dashboard"
            )

            st.write(
                "Export Reports"
            )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button(
            "Approve Backlog"
        )

    with col2:
        st.button(
            "Edit Backlog"
        )

    with col3:
        st.button(
            "Export JSON"
        )