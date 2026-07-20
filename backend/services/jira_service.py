from backend.integrations.jira_client import JiraClient
import json

client = JiraClient()


def push_project(project):
    """
    Push nested backlog to Jira.

    Hierarchy produced in Jira:

    Epic
        ├── Feature
        ├── Story
        │      └── Subtasks
        └── Story

    (Stories are created under the Epic because Jira does not allow
    Feature -> Story parenting in your project.)
    """

    created = {
        "epics": [],
        "features": [],
        "stories": [],
        "tasks": []
    }

    print("\n========== PUSH PROJECT STARTED ==========\n")

    for epic in project.get("epics", []):

        print(f"Creating Epic: {epic['title']}")

        epic_description = epic.get("description", "")

        epic_issue = client.create_issue(
            summary=epic["title"],
            description=epic_description,
            issue_type="Epic"
        )

        epic_key = epic_issue["key"]

        created["epics"].append(epic_key)

        print(f"Created Epic -> {epic_key}")

        ##################################################
        # FEATURES
        ##################################################

        for feature in epic.get("features", []):

            print(f"Creating Feature: {feature['title']}")

            feature_issue = client.create_issue(
                summary=feature["title"],
                description=feature.get("description", ""),
                issue_type="Feature",
                parent_key=epic_key
            )

            feature_key = feature_issue["key"]

            created["features"].append(feature_key)

            print(f"Created Feature -> {feature_key}")

            ##################################################
            # STORIES
            ##################################################

            for story in feature.get("user_stories", []):

                print(f"Creating Story: {story['title']}")

                acceptance = "\n".join(
                    story.get("acceptance_criteria", [])
                )

                story_description = f"""
As a:
{story.get('as_a','')}

I want:
{story.get('i_want','')}

So that:
{story.get('so_that','')}

Priority:
{story.get('priority','')}

Story Points:
{story.get('story_points','')}

Acceptance Criteria:
{acceptance}
"""

                story_issue = client.create_issue(
                    summary=story["title"],
                    description=story_description,
                    issue_type="Story",
                    parent_key=epic_key
                )

                story_key = story_issue["key"]

                created["stories"].append(story_key)

                print(f"Created Story -> {story_key}")

                ##############################################
                # TASKS
                ##############################################

                for task in story.get("tasks", []):

                    print(f"Creating Task: {task['title']}")

                    task_description = f"""
Description

{task.get('description','')}

Estimated Hours

{task.get('estimated_hours','')}
"""

                    task_issue = client.create_issue(
                        summary=task["title"],
                        description=task_description,
                        issue_type="Subtask",
                        parent_key=story_key
                    )

                    created["tasks"].append(task_issue["key"])

                    print(f"Created Task -> {task_issue['key']}")

    print("\n========== PUSH PROJECT FINISHED ==========\n")
    print(json.dumps(created, indent=4))

    return created