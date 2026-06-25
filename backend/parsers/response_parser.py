import json


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
        return json.loads(response_text)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Invalid JSON returned by Gemini:\n\n{response_text}"
        ) from e