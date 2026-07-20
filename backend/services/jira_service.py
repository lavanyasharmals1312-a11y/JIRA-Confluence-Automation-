from backend.integrations.jira_client import JiraClient
import json

client = JiraClient()


def push_project(project):
    """
    Pushes the new flat backlog structure to Jira.

    Expected JSON:

    {
        "epics": [],
        "features": [],
        "stories": [],
        "tasks": []
    }
    """

    created = {
        "epics": [],
        "features": [],
        "stories": [],
        "tasks": []
    }

    # Mapping dictionaries

    epic_keys = {}
    feature_keys = {}
    story_keys = {}

    print("\n================ PUSH PROJECT STARTED ================\n")

    ###############################################################
    # CREATE EPICS
    ###############################################################

    for epic in project.get("epics", []):

        print(f"\nCreating Epic : {epic['title']}")

        description = f"""
Epic ID

{epic.get("epic_id","")}

Description

{epic.get("description","")}

Business Value

{epic.get("business_value","")}
"""

        try:

            issue = client.create_issue(

                summary=f"{epic['epic_id']} - {epic['title']}",

                description=description,

                issue_type="Epic"

            )

            epic_key = issue["key"]

            epic_keys[epic["epic_id"]] = epic_key

            created["epics"].append(epic_key)

            print(f"Created Epic -> {epic_key}")

        except Exception as e:

            print("FAILED TO CREATE EPIC")

            print(epic["title"])

            raise e

    ###############################################################
    # CREATE FEATURES
    ###############################################################

    for feature in project.get("features", []):

        print(f"\nCreating Feature : {feature['title']}")

        parent_key = epic_keys.get(feature["epic_id"])

        if parent_key is None:

            raise Exception(
                f"No Epic found for {feature['feature_id']}"
            )

        feature_description = f"""
Feature ID

{feature.get("feature_id","")}

Description

{feature.get("description","")}

Estimated Sprint

{feature.get("estimated_sprint","")}

Acceptance Criteria

{chr(10).join(feature.get("acceptance_criteria", []))}
"""

        try:

            issue = client.create_issue(

                summary=f"{feature['feature_id']} - {feature['title']}",

                description=feature_description,

                issue_type="Story",

                parent_key=parent_key

            )

            feature_key = issue["key"]

            feature_keys[feature["feature_id"]] = feature_key

            created["features"].append(feature_key)

            print(f"Created Feature -> {feature_key}")

        except Exception as e:

            print("FAILED TO CREATE FEATURE")

            print(feature["title"])

            raise e
    ###############################################################
    # CREATE STORIES
    ###############################################################

    for story in project.get("stories", []):

        print(f"\nCreating Story : {story['title']}")

        parent_key = feature_keys.get(story["feature_id"])

        if parent_key is None:

            raise Exception(
                f"No Feature found for {story['story_id']}"
            )

        ###########################################################
        # Collect tasks belonging to this story
        ###########################################################

        related_tasks = []

        for task in project.get("tasks", []):

            if task.get("story_id") == story.get("story_id"):

                related_tasks.append(task)

        ###########################################################
        # Build task text
        ###########################################################

        task_text = ""

        for task in related_tasks:

            task_text += f"""

Task ID

{task.get("task_id","")}

Title

{task.get("title","")}

Description

{task.get("description","")}

Estimated Hours

{task.get("estimated_hours","")}

----------------------------------------
"""

        ###########################################################
        # Story description
        ###########################################################

        story_description = f"""
Story ID

{story.get("story_id","")}

As a

{story.get("as_a","")}

I want

{story.get("i_want","")}

So that

{story.get("so_that","")}

Priority

{story.get("priority","")}

Story Points

{story.get("story_points","")}

Acceptance Criteria

{chr(10).join(story.get("acceptance_criteria", []))}

Implementation Tasks

{task_text}
"""

        try:

            issue = client.create_issue(

                summary=f"{story['story_id']} - {story['title']}",

                description=story_description,

                issue_type="Story",

                parent_key=parent_key

            )

            story_key = issue["key"]

            story_keys[story["story_id"]] = story_key

            created["stories"].append(story_key)

            print(f"Created Story -> {story_key}")

        except Exception as e:

            print("FAILED TO CREATE STORY")

            print(story["title"])

            raise e

    ###############################################################
    # CREATE TASKS AS SUB-TASKS
    ###############################################################

    for task in project.get("tasks", []):

        print(f"\nCreating Task : {task['title']}")

        parent_key = story_keys.get(task["story_id"])

        if parent_key is None:

            raise Exception(
                f"No Story found for {task['task_id']}"
            )

        task_description = f"""
Task ID

{task.get("task_id","")}

Description

{task.get("description","")}

Estimated Hours

{task.get("estimated_hours","")}
"""

        try:

            issue = client.create_issue(

                summary=f"{task['task_id']} - {task['title']}",

                description=task_description,

                issue_type="Sub-task",

                parent_key=parent_key

            )

            created["tasks"].append(issue["key"])

            print(f"Created Task -> {issue['key']}")

        except Exception as e:

            print("FAILED TO CREATE TASK")

            print(task["title"])

            raise e

    print("\n================ PUSH PROJECT FINISHED ================\n")

    print(json.dumps(created, indent=4))

    return created