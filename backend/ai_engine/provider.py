import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from backend.config.config_manager import load_config

# Load local .env if present
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(env_path)

# Try importing Streamlit (works only inside the app)
try:
    import streamlit as st
except ImportError:
    st = None


class GeminiProvider:

    def __init__(self):

        config = load_config()

        api_key = config.get("gemini_api_key")

        # Fall back to .env
        if not api_key:
            api_key = os.getenv("GEMINI_API_KEY")

        # Fall back to Streamlit Secrets
        if (not api_key) and st is not None:
            try:
                api_key = st.secrets.get("GEMINI_API_KEY")
            except Exception:
                pass

        if not api_key:
            raise ValueError(
                "No Gemini API key found. Configure GEMINI_API_KEY in .env (local) or Streamlit Secrets (cloud)."
            )

        self.client = genai.Client(api_key=api_key)

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

        print("\n================ GEMINI MODEL ================\n")
        print(self.model)

        print("\n================ PROMPT LENGTH ================\n")
        print(len(prompt))

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
                response_mime_type="application/json"
            )
        )

        print("\n================ RESPONSE LENGTH ================\n")

        try:
            print(len(response.text))
        except Exception:
            print("Unable to determine response length.")

        print("\n================ RESPONSE TEXT ================\n")

        try:
            print(response.text)
        except Exception as e:
            print("Unable to print response.text")
            print(e)

        print("\n================ FULL RESPONSE OBJECT ================\n")

        print(response)

        print("\n================ CANDIDATES ================\n")

        try:
            print(response.candidates)
        except Exception as e:
            print(e)

        print("\n================ USAGE METADATA ================\n")

        try:
            print(response.usage_metadata)
        except Exception as e:
            print(e)

        print("\n================ FINISH REASON ================\n")

        try:
            print(response.candidates[0].finish_reason)
        except Exception as e:
            print(e)

        # Save raw response to disk
        try:
            with open(
                "gemini_raw_response.json",
                "w",
                encoding="utf-8"
            ) as f:
                f.write(response.text)

            print("\nSaved raw response to gemini_raw_response.json\n")

        except Exception as e:
            print("Could not save response:", e)

        return response


class AzureProvider:

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        print("\n================ RAW RESPONSE ================\n")
        print(response)
        print("\n==============================================\n")

        print("\n================ RESPONSE TEXT ===============\n")
        print(getattr(response, "text", None))
        print("\n==============================================\n")

        return response


class ClaudeProvider:

    def generate(self, prompt):

        raise NotImplementedError(
            "Claude integration not implemented."
        )


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