import json


def parse_llm_response(response_text):

    try:
        data = json.loads(response_text)
        return data

    except Exception as e:
        print("Parsing Error:", e)
        return None