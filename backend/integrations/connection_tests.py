from google import genai

from backend.integrations.jira_client import JiraClient


def test_gemini_connection(api_key):
    """
    Test Gemini API connectivity using the provided API key.
    """

    try:

        client = genai.Client(api_key=api_key)

        client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Reply only with OK."
        )

        return True, "Gemini connection successful."

    except Exception as e:

        return False, str(e)


def test_jira_connection(
    email,
    api_token,
    base_url,
    project_key
):
    """
    Test Jira authentication and project access.
    """

    creds = {
        "email": email,
        "api_token": api_token,
        "base_url": base_url,
        "project_key": project_key
    }

    try:

        client = JiraClient(creds)

        success, result = client.test_connection()

        if not success:
            return False, result

        project = client.get_project()

        return (
            True,
            f"Connected successfully to project '{project['key']}'."
        )

    except Exception as e:

        return False, str(e)