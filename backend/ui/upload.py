import streamlit as st
import io
from pypdf import PdfReader


def show_upload():

    st.title("Requirement Ingestion")

    source = st.selectbox(
        "Requirement Source",
        [
            "File Upload",
            "Confluence (Coming Soon)"
        ]
    )

    uploaded_file = st.file_uploader(
        "Upload Requirement Document",
        type=["pdf", "txt"]
    )

    if uploaded_file:

        document = ""

        if uploaded_file.type == "text/plain":

            document = uploaded_file.read().decode(
                "utf-8"
            )

        else:

            pdf_reader = PdfReader(
                io.BytesIO(
                    uploaded_file.read()
                )
            )

            for page in pdf_reader.pages:

                text = page.extract_text()

                if text:
                    document += text

        st.success(
            "Document uploaded successfully."
        )

        st.text_area(
            "Document Preview",
            document,
            height=300
        )

        st.button(
            "Generate Backlog"
        )