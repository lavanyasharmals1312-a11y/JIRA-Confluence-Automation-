from backend.integrations.jira_client import JiraClient
import json

client = JiraClient()


def push_project(project):

    created = {
        "epics": [],
        "features": [],
        "stories": [],
        "subtasks": []
    }

    print("\n================ PUSH PROJECT STARTED ================\n")

    print("Project Keys:")
    print(project.keys())

    for epic in project.get("epics", []):

        print("\n===================================================")
        print(f"Creating Epic : {epic['title']}")
        print("===================================================\n")

        epic_issue = client.create_issue(
            summary=f"{epic['epic_id']} - {epic['title']}",
            description=epic.get("detailed_description", ""),
            issue_type="Epic"
        )

        epic_key = epic_issue["key"]

        print(f"Epic Created -> {epic_key}")

        created["epics"].append(epic_key)

        ##################################################
        # FEATURES
        ##################################################

        print(f"Feature Count : {len(epic.get('features', []))}")

        for feature in epic.get("features", []):

            print("\n--------------------------------------------------")
            print(f"Creating Feature : {feature['title']}")
            print("--------------------------------------------------")

            print("Feature Keys:")
            print(list(feature.keys()))

            print("Stories key exists:", "stories" in feature)

            stories = feature.get("stories", [])

            print("Story Count:", len(stories))

            feature_description = f"""
Feature ID

{feature.get('feature_id', '')}

Description

{feature.get('description', '')}

Feature Type

{feature.get('feature_type', '')}

Owner

{feature.get('feature_owner', '')}

Estimated Sprint

{feature.get('estimated_sprint', '')}
"""

            feature_issue = client.create_issue(
                summary=f"{feature['feature_id']} - {feature['title']}",
                description=feature_description,
                issue_type="Story",
                parent_key=epic_key
            )

            feature_key = feature_issue["key"]

            print(f"Feature Created -> {feature_key}")

            created["features"].append(feature_key)

            ##################################################
            # STORIES
            ##################################################

            for story in stories:

                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                print(f"Creating Story : {story['title']}")
                print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

                tasks_text = ""

                tasks = story.get("tasks", [])

                print(f"Task Count : {len(tasks)}")

                for task in tasks:

                    tasks_text += f"""
Task ID

{task.get('task_id','')}

Title

{task.get('title','')}

Description

{task.get('description','')}

Estimated Hours

{task.get('estimated_hours','')}

Definition Of Done

{task.get('definition_of_done','')}

----------------------------------------
"""

                story_description = f"""
Story ID

{story.get('story_id','')}

Description

{story.get('detailed_description','')}

As a

{story.get('as_a','')}

I want

{story.get('i_want','')}

So that

{story.get('so_that','')}

Priority

{story.get('priority','')}

Story Points

{story.get('story_points','')}

Estimated Effort

{story.get('estimated_effort','')}

Acceptance Criteria

{chr(10).join(story.get('acceptance_criteria', []))}

Tasks

{tasks_text}
"""

                try:

                    story_issue = client.create_issue(
                        summary=f"{story['story_id']} - {story['title']}",
                        description=story_description,
                        issue_type="Story",
                        parent_key=feature_key
                    )

                    story_key = story_issue["key"]

                    print(f"Story Created -> {story_key}")

                    created["stories"].append(story_key)
                    created["subtasks"].append(story_key)

                except Exception as e:

                    print("\nERROR CREATING STORY")
                    print(story["title"])
                    print(e)
                    raise

    print("\n================ PUSH PROJECT FINISHED ================\n")

    print(json.dumps(created, indent=4))

    return created