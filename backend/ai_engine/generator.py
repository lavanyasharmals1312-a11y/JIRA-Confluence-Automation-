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

Requirement Document

{requirement}
"""

    retries = 3

    for attempt in range(retries):

        try:

            response = provider.generate(
                full_prompt
            )

            return parse_gemini_response(
                response.text
            )

        except ServerError:

            if attempt == retries - 1:
                raise

            wait = (attempt + 1) * 5

            print(
                f"Retrying in {wait} seconds..."
            )

            time.sleep(wait)