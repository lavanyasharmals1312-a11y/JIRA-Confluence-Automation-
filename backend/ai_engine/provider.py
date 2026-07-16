import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

# --------------------------------------------------
# Load .env (Local Development)
# --------------------------------------------------

env_path = Path(__file__).resolve().parents[2] / ".env"

load_dotenv(env_path)

# --------------------------------------------------
# Streamlit (Cloud)
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

            api_key = st.secrets.get(
                "GEMINI_API_KEY"
            )

        if not api_key:

            raise ValueError(
                "No Gemini API key found."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = (

            os.getenv("GEMINI_MODEL")

            or (

                st.secrets.get(
                    "GEMINI_MODEL"
                )

                if st is not None

                else None

            )

            or "gemini-2.5-flash"

        )

    def generate(self, prompt):

        print("\n================ MODEL ================\n")
        print(self.model)

        print("\n================ PROMPT LENGTH ================\n")
        print(len(prompt))

        response = self.client.models.generate_content(

            model=self.model,

            contents=prompt

        )

        print("\n================ RAW RESPONSE ================\n")
        print(response)

        print("\n================ RESPONSE.TEXT ================\n")
        print(repr(getattr(response, "text", None)))

        print("\n================ RESPONSE DICT ================\n")

        try:
            print(response.model_dump())

        except Exception as e:
            print(e)

        print("\n===============================================\n")

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
# FACTORY
# ==================================================

def get_provider(provider_name):

    if provider_name == "Gemini":

        return GeminiProvider()

    if provider_name == "Azure OpenAI":

        return AzureProvider()

    if provider_name == "Claude":

        return ClaudeProvider()

    raise ValueError(
        f"Unknown provider: {provider_name}"
    )