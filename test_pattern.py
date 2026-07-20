from backend.integrations.jira_client import JiraClient

client = JiraClient()

EPIC_KEY = "RS-73"   # replace with a real Epic key

issue = client.create_issue(
    summary="Story Test",
    description="Testing Epic -> Story",
    issue_type="Story",
    parent_key=EPIC_KEY
)

print(issue)