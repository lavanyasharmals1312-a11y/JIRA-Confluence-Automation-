import io
import streamlit as st
from pypdf import PdfReader

from backend.services.backlog_service import (
    generate_project
)


def show_upload():

    # -------------------------------------------------
    # PAGE HEADER
    # -------------------------------------------------

    st.title("Upload Document")

    st.caption(
        "Upload a Business Requirement Document (BRD) to automatically generate an AI-powered Jira backlog."
    )

    st.divider()

    # -------------------------------------------------
    # PROJECT DETAILS
    # -------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        project_name = st.text_input(
            "Project Name",
            placeholder="e.g. Employee Leave Management System"
        )

    with col2:

        source = st.selectbox(
            "Requirement Source",
            [
                "PDF Document",
                "Text File",
                "Confluence (Coming Soon)"
            ]
        )

    col3, col4 = st.columns(2)

    with col3:

        provider = st.selectbox(
            "AI Provider",
            [
                "Gemini",
                "Azure OpenAI",
                "Claude"
            ]
        )

    with col4:

        output_format = st.selectbox(
            "Output Format",
            [
                "Jira Ready JSON",
                "Standard JSON"
            ]
        )

    st.divider()

    # -------------------------------------------------
    # FILE UPLOAD
    # -------------------------------------------------

    uploaded_file = st.file_uploader(
        "Upload Requirement Document",
        type=["pdf", "txt"],
        help="Supported formats: PDF and TXT"
    )

    if uploaded_file is None:
        return

    document = ""

    # -------------------------------------------------
    # TXT
    # -------------------------------------------------

    if uploaded_file.type == "text/plain":

        document = uploaded_file.read().decode("utf-8")

    # -------------------------------------------------
    # PDF
    # -------------------------------------------------

    elif uploaded_file.type == "application/pdf":

        pdf_reader = PdfReader(
            io.BytesIO(uploaded_file.read())
        )

        for page in pdf_reader.pages:

            text = page.extract_text()

            if text:

                document += text + "\n"

    st.success("Document uploaded successfully.")

    # -------------------------------------------------
    # PREVIEW
    # -------------------------------------------------

    with st.expander(
        "Preview Extracted Content",
        expanded=False
    ):

        st.text_area(
            "Requirement Content",
            document,
            height=300
        )

    st.divider()

    # -------------------------------------------------
    # SUMMARY
    # -------------------------------------------------

    st.subheader("Generation Summary")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Project",
            project_name if project_name else "Untitled"
        )

    with c2:

        st.metric(
            "Provider",
            provider
        )

    with c3:

        st.metric(
            "Output",
            output_format
        )

    st.divider()

    # -------------------------------------------------
    # GENERATE BACKLOG
    # -------------------------------------------------

    if st.button(
        "Generate Backlog",
        type="primary",
        width="stretch"
    ):

        try:

            with st.spinner(
                "Generating AI backlog..."
            ):

                project, filepath = generate_project(

                    requirement=document,

                    provider=provider,

                    project_name=project_name

                )

            st.success(
                f"Project '{project['project_name']}' generated successfully."
            )

            st.session_state.page = "Backlog Review"

            st.rerun()

        except Exception as e:

            st.error(
                f"Failed to generate backlog.\n\n{e}"
            )