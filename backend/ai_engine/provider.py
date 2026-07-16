import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# --------------------------------------------------
# Load Local .env
# --------------------------------------------------

env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

# --------------------------------------------------
# Streamlit Support
# --------------------------------------------------

try:
    import streamlit as st
except ImportError:
    st = None


# ==================================================
# GEMINI PROVIDER
# ==================================================

class GeminiProvider:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if (not api_key) and st is not None:
            api_key = st.secrets.get("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "No Gemini API key found. Configure GEMINI_API_KEY in .env or Streamlit Secrets."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = (
            os.getenv("GEMINI_MODEL")
            or (
                st.secrets.get("GEMINI_MODEL")
                if st is not None
                else None
            )
            or "gemini-2.5-flash"
        )

    def generate(self, prompt):

        response = self.client.models.generate_content(

            model=self.model,

            contents=prompt,

            config={
                "response_mime_type": "application/json"
            }

        )

        print("\n================ MODEL ================")
        print(self.model)

        print("\n================ RESPONSE ================")
        print(response)

        print("\n================ RESPONSE TEXT ================")
        print(repr(response.text))

        print("=========================================\n")

        return response


# ==================================================
# AZURE
# ==================================================

class AzureProvider:

    def generate(self, prompt):

        raise NotImplementedError(
            "Azure OpenAI integration not implemented."
        )


# ==================================================
# CLAUDE
# ==================================================

class ClaudeProvider:

    def generate(self, prompt):

        raise NotImplementedError(
            "Claude integration not implemented."
        )


# ==================================================
# PROVIDER FACTORY
# ==================================================

def get_provider(provider_name):

    if provider_name == "Gemini":
        return GeminiProvider()

    elif provider_name == "Azure OpenAI":
        return AzureProvider()

    elif provider_name == "Claude":
        return ClaudeProvider()

    raise ValueError(
        f"Unknown provider: {provider_name}"
    )