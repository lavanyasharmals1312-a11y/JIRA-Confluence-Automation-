import json

from backend.utils.sanitize import sanitize_backlog


def parse_gemini_response(response_text):
    """
    Cleans Gemini output and converts it into a Python dictionary.
    """

    response_text = response_text.strip()

    # Remove Markdown code fences if present
    if response_text.startswith("```json"):
        response_text = response_text.replace("```json", "", 1)

    if response_text.startswith("```"):
        response_text = response_text.replace("```", "", 1)

    if response_text.endswith("```"):
        response_text = response_text[:-3]

    response_text = response_text.strip()

    try:
        parsed = json.loads(response_text)

        return sanitize_backlog(parsed)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON returned by Gemini:\n\n{response_text}"
        ) from e