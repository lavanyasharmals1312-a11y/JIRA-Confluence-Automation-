import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

env_path = (
    Path(__file__).resolve().parents[2] / ".env"
)

load_dotenv(env_path)


class GeminiProvider:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash"
        )

    def generate(self, prompt):

        return self.client.models.generate_content(

            model=self.model,

            contents=prompt
        )


class AzureProvider:

    def generate(self, prompt):

        raise NotImplementedError(
            "Azure OpenAI integration not implemented."
        )


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