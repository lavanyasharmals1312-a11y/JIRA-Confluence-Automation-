from backend.integrations.jira_client import JiraClient

client = JiraClient()

issue = client.create_issue(
    summary="AI Integration Test",
    description="Created from Python using the Jira REST API.",
    issue_type="Task"
)

print(issue)