from backend.integrations.jira_client import JiraClient


client = JiraClient()


def push_project(project):

    created = {

        "epics": [],

        "features": [],

        "stories": []

    }

    for epic in project.get("epics", []):

        print(

            f"Creating Epic : {epic['title']}"

        )

        epic_issue = client.create_issue(

            summary=f"{epic['epic_id']} - {epic['title']}",

            description=epic.get(

                "description",

                ""

            ),

            issue_type="Epic"

        )

        epic_key = epic_issue["key"]

        created["epics"].append(

            epic_key

        )

        # ------------------------------------------
        # FEATURES
        # ------------------------------------------

        for feature in epic.get(

            "features",

            []

        ):

            print(

                f"Creating Feature : {feature['title']}"

            )

            feature_description = f"""

Feature ID : {feature.get('feature_id','')}

Description

{feature.get('description','')}

Feature Type

{feature.get('feature_type','')}

Owner

{feature.get('feature_owner','')}

Estimated Sprint

{feature.get('estimated_sprint','')}
"""

            feature_issue = client.create_issue(

                summary=f"{feature['feature_id']} - {feature['title']}",

                description=feature_description,

                issue_type="Story",

                parent_key=epic_key

            )

            feature_key = feature_issue["key"]

            created["features"].append(

                feature_key

            )

            # ------------------------------------------
            # USER STORIES
            # ------------------------------------------

            for story in feature.get(

                "user_stories",

                []

            ):

                print(

                    f"Creating Story : {story['title']}"

                )

                tasks = ""

                for task in story.get(

                    "tasks",

                    []

                ):

                    tasks += f"""

{task.get('task_id','')}

{task.get('title','')}

{task.get('description','')}

Estimated Hours : {task.get('estimated_hours','')}

Definition Of Done :

{task.get('definition_of_done','')}

----------------------------------------
"""

                story_description = f"""

Story ID

{story.get('story_id','')}

Description

{story.get('description','')}

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

{chr(10).join(story.get('acceptance_criteria',[]))}

Tasks

{tasks}
"""

                story_issue = client.create_issue(

                    summary=f"{story['story_id']} - {story['title']}",

                    description=story_description,

                    issue_type="Subtask",

                    parent_key=feature_key

                )

                created["stories"].append(

                    story_issue["key"]

                )

    return created