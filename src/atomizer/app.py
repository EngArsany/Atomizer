import os
import logging
import requests
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path

from atomizer.config import configure_logging

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env", override=True)

configure_logging()
logger = logging.getLogger(__name__)

API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")


def generate_notes(pdf_file) -> list[str]:
    """Send the uploaded PDF to the FastAPI backend."""
    logger.debug("Creating Headers")
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
    }
    logger.info("Headers Created")

    files = {
        "file": (
            pdf_file.name,
            pdf_file.getvalue(),
            "application/pdf",
        )
    }
    logger.info("File Uploaded")

    logger.debug("Sending Request")
    response = requests.post(
        API_URL,
        headers=headers,
        files=files,
        timeout=300,
    )
    logger.info("Request Sent!")

    response.raise_for_status()
    return response.json()["contents"]


def main() -> None:
    st.set_page_config(
        page_title="Atomizer",
        page_icon="⚛️",
        layout="centered",
    )

    st.markdown(
        """
        <style>
        /* Main page */
        .stApp {
            background: #0b1020;
        }

        .block-container {
            max-width: 850px;
            padding-top: 3rem;
            padding-bottom: 4rem;
        }

        /* Header */
        .atomizer-header {
            text-align: center;
            margin-bottom: 2.5rem;
        }

        .atom-icon {
            font-size: 4rem;
            line-height: 1;
            margin-bottom: 0.75rem;
        }

        .atomizer-title {
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: -0.04em;
            color: #f8fafc;
            margin: 0;
        }

        .atomizer-subtitle {
            color: #94a3b8;
            font-size: 1.05rem;
            margin-top: 0.5rem;
        }

        /* Upload area */
        [data-testid="stFileUploader"] {
            background: #11182b;
            border: 1px solid #26324d;
            border-radius: 16px;
            padding: 1rem;
        }

        [data-testid="stFileUploaderDropzone"] {
            background: #0e1527;
            border: 1px dashed #475569;
            border-radius: 12px;
        }

        [data-testid="stFileUploaderDropzone"]:hover {
            border-color: #818cf8;
        }

        /* Generate button */
        .stButton > button {
            width: 100%;
            height: 3.2rem;
            border-radius: 10px;
            border: none;
            background: #6366f1;
            color: white;
            font-size: 1rem;
            font-weight: 600;
            transition: 0.2s ease;
        }

        .stButton > button:hover {
            background: #818cf8;
            border: none;
            color: white;
        }

        /* Result area */
        .notes-header {
            color: #f8fafc;
            margin-top: 2.5rem;
        }

        [data-testid="stMarkdownContainer"] {
            color: #dbe4f0;
        }

        /* Divider */
        hr {
            border-color: #26324d;
        }

        /* Hide Streamlit branding */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Header
    st.markdown(
        """
        <div class="atomizer-header">
            <div class="atom-icon">⚛️</div>
            <div class="atomizer-title">Atomizer</div>
            <div class="atomizer-subtitle">
                Transform documents into atomic knowledge
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Upload
    pdf_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        help="Upload a PDF document to generate atomic knowledge notes.",
    )

    st.write("")

    # Generate
    if st.button(
        "Generate Notes",
        type="primary",
        disabled=pdf_file is None,
    ):
        with st.spinner("Atomizing your document..."):
            try:
                notes = generate_notes(pdf_file)

                st.success("Your notes are ready.")

                st.markdown(
                    '<h2 class="notes-header">Generated Notes</h2>',
                    unsafe_allow_html=True,
                )

                for note in notes:
                    st.markdown(note)
                    st.divider()

            except requests.exceptions.HTTPError as error:
                status_code = error.response.status_code
                detail = error.response.text

                st.error(f"API request failed ({status_code}): {detail}")

            except requests.exceptions.RequestException as error:
                st.error(f"Could not connect to the API: {error}")

            except (KeyError, ValueError) as error:
                st.error(f"Invalid API response: {error}")


if __name__ == "__main__":
    main()
