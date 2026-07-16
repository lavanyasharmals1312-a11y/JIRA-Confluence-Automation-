import time

from google.genai.errors import ServerError

from backend.ai_engine.provider import (
    get_provider
)

from backend.parsers.response_parser import (
    parse_gemini_response
)


def generate_backlog(

    prompt,

    requirement,

    provider_name="Gemini"

):

    provider = get_provider(
        provider_name
    )

    full_prompt = f"""
{prompt}

------------------------------------------------------------

REQUIREMENT DOCUMENT

------------------------------------------------------------

{requirement}
"""

    retries = 3

    for attempt in range(retries):

        try:

            response = provider.generate(
                full_prompt
            )

            if response is None:

                raise ValueError(
                    "Gemini returned no response."
                )

            if not hasattr(response, "text"):

                raise ValueError(
                    "Gemini response has no text attribute."
                )

            if response.text is None:

                raise ValueError(
                    "Gemini returned a null response."
                )

            if not response.text.strip():

                raise ValueError(
                    "Gemini returned an empty response."
                )

            print("\n================ RAW GEMINI RESPONSE ================\n")
            print(response.text)
            print("\n=====================================================\n")

            project = parse_gemini_response(
                response.text
            )

            if not isinstance(project, dict):

                raise ValueError(
                    "Parsed response is not a JSON object."
                )

            return project

        except ServerError:

            if attempt == retries - 1:
                raise

            wait = (attempt + 1) * 5

            print(
                f"Retrying in {wait} seconds..."
            )

            time.sleep(wait)