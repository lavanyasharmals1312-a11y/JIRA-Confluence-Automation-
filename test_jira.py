from backend.integrations.jira_client import JiraClient

client = JiraClient()

meta = client.get_create_metadata()

for issue in meta["projects"][0]["issuetypes"]:
    print(issue["name"], issue["hierarchyLevel"])