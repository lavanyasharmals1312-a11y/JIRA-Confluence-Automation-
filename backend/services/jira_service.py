from backend.integrations.jira_client import JiraClient


client = JiraClient()


def push_project(project):

    created = {

        "epics": [],

        "stories": [],

        "subtasks": []

    }

    for epic in project["epics"]:

        print(f"Creating Epic: {epic['title']}")

        epic_issue = client.create_issue(

            summary=epic["title"],

            description=epic["description"],

            issue_type="Epic"

        )

        epic_key = epic_issue["key"]

        created["epics"].append(epic_key)

        for story in epic["stories"]:

            print(f"Creating Story: {story['title']}")

            story_issue = client.create_issue(

                summary=story["title"],

                description=story["description"],

                issue_type="Story",

                parent_key=epic_key

            )

            story_key = story_issue["key"]

            created["stories"].append(story_key)

            for task in story["tasks"]:

                print(f"Creating Subtask: {task['title']}")

                subtask_issue = client.create_issue(

                    summary=task["title"],

                    description=task["description"],

                    issue_type="Subtask",

                    parent_key=story_key

                )

                created["subtasks"].append(

                    subtask_issue["key"]

                )

    return created