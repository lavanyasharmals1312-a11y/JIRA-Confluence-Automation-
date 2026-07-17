import io
import streamlit as st
from pypdf import PdfReader

from backend.services.backlog_service import (
    generate_project
)


def show_upload():

    # =====================================================
    # PAGE HEADER
    # =====================================================

    st.markdown(
        """
        <div style="
            background:linear-gradient(135deg,#2563EB,#4F46E5);
            padding:32px;
            border-radius:20px;
            color:white;
            margin-bottom:30px;
            box-shadow:0 10px 28px rgba(37,99,235,.22);
        ">

            <div style="
                font-size:34px;
                font-weight:800;
                margin-bottom:8px;
            ">
                Upload Requirement Document
            </div>

            <div style="
                font-size:17px;
                opacity:.92;
            ">
                Upload a Business Requirement Document and automatically generate
                Epics, Features, User Stories and Tasks using AI.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # PROJECT CONFIGURATION
    # =====================================================

    left, right = st.columns([2, 1], gap="large")

    with left:

        st.markdown("## Project Configuration")

        project_name = st.text_input(
            "Project Name",
            placeholder="Employee Leave Management System"
        )

        source = st.selectbox(
            "Requirement Source",
            [
                "PDF Document",
                "Text File",
                "Confluence (Coming Soon)"
            ]
        )

        uploaded_file = st.file_uploader(
            "Requirement Document",
            type=["pdf", "txt"],
            help="Supported formats: PDF and TXT"
        )

    with right:

        st.markdown("## AI Configuration")

        provider = st.selectbox(
            "AI Provider",
            [
                "Gemini",
                "Azure OpenAI",
                "Claude"
            ]
        )

        output_format = st.selectbox(
            "Output Format",
            [
                "Jira Ready JSON",
                "Standard JSON"
            ]
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            f"""
            <div style="
                background:white;
                border:1px solid #E5E7EB;
                border-radius:18px;
                padding:22px;
                box-shadow:0 6px 20px rgba(0,0,0,.05);
            ">

                <div style="
                    font-size:18px;
                    font-weight:700;
                    margin-bottom:18px;
                    color:#0F172A;
                ">
                    Configuration Summary
                </div>

                <table style="width:100%;font-size:15px;">

                    <tr>
                        <td style="padding-bottom:10px;"><b>Provider</b></td>
                        <td style="text-align:right;">{provider}</td>
                    </tr>

                    <tr>
                        <td style="padding-bottom:10px;"><b>Output</b></td>
                        <td style="text-align:right;">{output_format}</td>
                    </tr>

                    <tr>
                        <td><b>Source</b></td>
                        <td style="text-align:right;">{source}</td>
                    </tr>

                </table>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # FILE PROCESSING
    # =====================================================

    if uploaded_file is None:
        return

    document = ""

    if uploaded_file.type == "text/plain":

        document = uploaded_file.read().decode("utf-8")

    elif uploaded_file.type == "application/pdf":

        pdf_reader = PdfReader(
            io.BytesIO(uploaded_file.read())
        )

        for page in pdf_reader.pages:

            text = page.extract_text()

            if text:
                document += text + "\n"

    st.success("Requirement document uploaded successfully.")
    # =====================================================
    # DOCUMENT PREVIEW
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("## Document Preview")

    st.markdown(
        """
        <div style="
            background:white;
            border:1px solid #E5E7EB;
            border-radius:18px;
            padding:18px;
            margin-bottom:20px;
            box-shadow:0 6px 20px rgba(0,0,0,.05);
        ">
            Review the extracted requirement content before generating the project backlog.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.text_area(
        "",
        document,
        height=320,
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # GENERATION SUMMARY
    # =====================================================

    st.markdown("## Generation Summary")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            f"""
            <div style="
                background:white;
                border-radius:18px;
                padding:24px;
                border:1px solid #E5E7EB;
                box-shadow:0 6px 18px rgba(0,0,0,.05);
                min-height:120px;
            ">
                <div style="
                    color:#64748B;
                    font-size:14px;
                    font-weight:600;
                ">
                    PROJECT
                </div>

                <div style="
                    margin-top:12px;
                    font-size:24px;
                    font-weight:700;
                    color:#0F172A;
                ">
                    {project_name if project_name else "Untitled Project"}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:

        st.markdown(
            f"""
            <div style="
                background:white;
                border-radius:18px;
                padding:24px;
                border:1px solid #E5E7EB;
                box-shadow:0 6px 18px rgba(0,0,0,.05);
                min-height:120px;
            ">
                <div style="
                    color:#64748B;
                    font-size:14px;
                    font-weight:600;
                ">
                    AI PROVIDER
                </div>

                <div style="
                    margin-top:12px;
                    font-size:24px;
                    font-weight:700;
                    color:#0F172A;
                ">
                    {provider}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:

        st.markdown(
            f"""
            <div style="
                background:white;
                border-radius:18px;
                padding:24px;
                border:1px solid #E5E7EB;
                box-shadow:0 6px 18px rgba(0,0,0,.05);
                min-height:120px;
            ">
                <div style="
                    color:#64748B;
                    font-size:14px;
                    font-weight:600;
                ">
                    OUTPUT FORMAT
                </div>

                <div style="
                    margin-top:12px;
                    font-size:24px;
                    font-weight:700;
                    color:#0F172A;
                ">
                    {output_format}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # =====================================================
    # GENERATE SECTION
    # =====================================================

    st.markdown(
        """
        <div style="
            background:white;
            border-radius:20px;
            border:1px solid #E5E7EB;
            padding:28px;
            box-shadow:0 8px 22px rgba(0,0,0,.05);
            text-align:center;
            margin-bottom:20px;
        ">

            <div style="
                font-size:26px;
                font-weight:700;
                color:#0F172A;
                margin-bottom:10px;
            ">
                Ready to Generate
            </div>

            <div style="
                color:#64748B;
                font-size:16px;
            ">
                Generate a complete project backlog consisting of
                Epics, Features, User Stories and Tasks.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    generate = st.button(
        "Generate Backlog",
        use_container_width=True,
        type="primary"
    )

    if generate:

        try:

            with st.spinner("Generating project backlog..."):

                project, filepath = generate_project(

                    requirement=document,

                    provider=provider,

                    project_name=project_name

                )

            st.success(
                f"Project '{project.get('project_name','Untitled Project')}' generated successfully."
            )

            st.session_state.page = "Backlog Review"

            st.rerun()

        except Exception as e:

            st.exception(e)