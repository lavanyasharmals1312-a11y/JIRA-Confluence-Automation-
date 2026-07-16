import json


def parse_gemini_response(response_text):
    """
    Cleans Gemini output and converts it into a Python dictionary.
    Raises clear errors if the response is invalid.
    """

    if response_text is None:

        raise ValueError(
            "Gemini returned no response."
        )

    response_text = response_text.strip()

    if not response_text:

        raise ValueError(
            "Gemini returned an empty response."
        )

    # -----------------------------------------
    # Remove Markdown Code Blocks
    # -----------------------------------------

    if response_text.startswith("```json"):

        response_text = response_text.replace(
            "```json",
            "",
            1
        )

    elif response_text.startswith("```"):

        response_text = response_text.replace(
            "```",
            "",
            1
        )

    if response_text.endswith("```"):

        response_text = response_text[:-3]

    response_text = response_text.strip()

    # -----------------------------------------
    # Parse JSON
    # -----------------------------------------

    try:

        data = json.loads(
            response_text
        )

    except json.JSONDecodeError as e:

        print("\n=========== RAW GEMINI RESPONSE ===========\n")
        print(response_text)
        print("\n===========================================\n")

        raise ValueError(
            "Gemini returned invalid JSON."
        ) from e

    # -----------------------------------------
    # Validate Root Object
    # -----------------------------------------

    if not isinstance(data, dict):

        raise ValueError(
            "Gemini response is not a JSON object."
        )

    # -----------------------------------------
    # Validate Required Keys
    # -----------------------------------------

    required_keys = [

        "project_name",

        "project_description",

        "executive_summary",

        "document_version",

        "generated_by",

        "generated_on",

        "status",

        "epics"

    ]

    missing = [

        key

        for key in required_keys

        if key not in data

    ]

    if missing:

        raise ValueError(

            "Gemini response is missing required keys: "

            + ", ".join(missing)

        )

    if not isinstance(
        data["epics"],
        list
    ):

        raise ValueError(
            "'epics' must be a list."
        )

    return data