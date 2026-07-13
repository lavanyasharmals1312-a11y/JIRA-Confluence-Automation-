from backend.integrations.jira_client import JiraClient

client = JiraClient()


def format_epic_description(epic):

    description = f"""
Business Objective
------------------
{epic["business_objective"]}

Business Value
--------------
{epic["business_value"]}

Description
-----------
{epic["description"]}

Scope
-----
"""

    for item in epic["scope"]:
        description += f"\n• {item}"

    description += "\n\nOut of Scope\n------------"

    for item in epic["out_of_scope"]:
        description += f"\n• {item}"

    description += "\n\nAssumptions\n-----------"

    for item in epic["assumptions"]:
        description += f"\n• {item}"

    description += "\n\nDependencies\n------------"

    for item in epic["dependencies"]:
        description += f"\n• {item}"

    description += "\n\nRisks\n-----"

    for item in epic["risks"]:
        description += f"\n• {item}"

    description += "\n\nAcceptance Criteria\n-------------------"

    for item in epic["acceptance_criteria"]:
        description += f"\n• {item}"

    return description


def format_story_description(story):

    description = f"""
Description
-----------
{story["description"]}

User Story
----------

As a
{story["as_a"]}

I want
{story["i_want"]}

So that
{story["so_that"]}

Priority
--------
{story["priority"]}

Story Points
------------
{story["story_points"]}

Acceptance Criteria
-------------------
"""

    for item in story["acceptance_criteria"]:
        description += f"\n• {item}"

    return description


def format_task_description(task):

    return f"""
Description
-----------
{task["description"]}

Definition of Done
------------------
{task["definition_of_done"]}
"""


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

            description=format_epic_description(epic),

            issue_type="Epic"

        )

        epic_key = epic_issue["key"]

        created["epics"].append(epic_key)

        for story in epic["stories"]:

            print(f"Creating Story: {story['title']}")

            story_issue = client.create_issue(

                summary=story["title"],

                description=format_story_description(story),

                issue_type="Story",

                parent_key=epic_key

            )

            story_key = story_issue["key"]

            created["stories"].append(story_key)

            for task in story["tasks"]:

                print(f"Creating Subtask: {task['title']}")

                subtask_issue = client.create_issue(

                    summary=task["title"],

                    description=format_task_description(task),

                    issue_type="Subtask",

                    parent_key=story_key

                )

                created["subtasks"].append(

                    subtask_issue["key"]

                )

    return created