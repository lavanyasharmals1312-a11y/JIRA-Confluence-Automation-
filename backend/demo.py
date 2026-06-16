import streamlit as st
import io
from pypdf import PdfReader

st.set_page_config(
    page_title="AI Requirement to Jira Backlog Generator",
    layout="wide"
)

st.title("AI Requirement to Jira Backlog Generator")

st.write(
    "Upload a requirement document and automatically generate Epics, User Stories, and Tasks."
)

uploaded_file = st.file_uploader(
    "Upload Requirement Document",
    type=["txt", "pdf"]
)

if uploaded_file:

    document = ""

    # TXT SUPPORT
    if uploaded_file.type == "text/plain":

        document = uploaded_file.read().decode("utf-8")

    # PDF SUPPORT
    elif uploaded_file.type == "application/pdf":

        pdf_reader = PdfReader(
            io.BytesIO(uploaded_file.read())
        )

        for page in pdf_reader.pages:

            page_text = page.extract_text()

            if page_text:
                document += page_text + "\n"

    st.success("Document uploaded successfully!")

    with st.expander("Preview Extracted Text"):
        st.text_area(
            "Document Content",
            document,
            height=250
        )

    if st.button("Generate Backlog"):

        # Demo data based on previously generated CRM output
        data = {

            "epics": [
                "Lead Management",
                "Customer Communication & Engagement",
                "Sales & Performance Analytics"
            ],

            "stories": [
                {
                    "epic": "Lead Management",
                    "story": "As a Sales Executive, I want to create new leads so that I can capture potential customer information."
                },

                {
                    "epic": "Lead Management",
                    "story": "As a Sales Executive, I want to update lead details so that I can keep information current."
                },

                {
                    "epic": "Customer Communication & Engagement",
                    "story": "As a CRM System, I want to automatically send welcome emails to new customers."
                },

                {
                    "epic": "Sales & Performance Analytics",
                    "story": "As a Sales Manager, I want to view sales performance reports."
                }
            ],

            "tasks": [
                {
                    "story": "Create new leads",
                    "task": "Design Lead Entry Form"
                },

                {
                    "story": "Create new leads",
                    "task": "Develop POST /leads API endpoint"
                },

                {
                    "story": "Welcome Email Automation",
                    "task": "Integrate Email Service Provider"
                },

                {
                    "story": "Welcome Email Automation",
                    "task": "Create Welcome Email Template"
                },

                {
                    "story": "Sales Reports",
                    "task": "Build Sales Dashboard"
                },

                {
                    "story": "Sales Reports",
                    "task": "Generate KPI Analytics"
                }
            ]
        }

        st.header("Epics")

        for epic in data["epics"]:
            st.subheader(epic)

        st.divider()

        st.header("User Stories")

        for story in data["stories"]:

            st.markdown(
                f"**Epic:** {story['epic']}"
            )

            st.write(
                story["story"]
            )

            st.divider()

        st.header("Tasks")

        for task in data["tasks"]:

            st.markdown(
                f"**Task:** {task['task']}"
            )

            st.write(
                f"Related Story: {task['story']}"
            )

            st.divider()

        st.success(
            "Backlog generated successfully!"
        )