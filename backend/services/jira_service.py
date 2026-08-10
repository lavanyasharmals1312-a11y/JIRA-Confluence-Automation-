from backend.integrations.jira_client import JiraClient
import json


client = JiraClient()


# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------

def format_list(items):

    if not items:
        return "None"

    return "\n".join(
        f"• {item}"
        for item in items
    )


def build_project_context(project):

    summary = project.get(
        "executive_summary",
        {}
    )

    planning = project.get(
        "planning",
        {}
    )

    return f"""
BUSINESS DETAILS

Project Overview:
{summary.get("project_overview", "")}

Business Problem:
{summary.get("business_problem", "")}

Business Need:
{summary.get("business_need", "")}

Project Vision:
{summary.get("project_vision", "")}

Business Goals:
{format_list(summary.get("business_goals", []))}

Target Users:
{format_list(summary.get("target_users", []))}

Business Benefits:
{format_list(summary.get("business_benefits", []))}

Expected Outcome:
{summary.get("expected_outcome", "")}

Success Criteria:
{format_list(summary.get("success_criteria", []))}


SCOPE & PLANNING

Project Scope:
{planning.get("project_scope", "")}

In Scope:
{format_list(planning.get("in_scope", []))}

Out of Scope:
{format_list(planning.get("out_of_scope", []))}

Assumptions:
{format_list(planning.get("assumptions", []))}

Dependencies:
{format_list(planning.get("dependencies", []))}

Constraints:
{format_list(planning.get("constraints", []))}

Risks:
{format_list(planning.get("risks", []))}

Stakeholders:
{format_list(planning.get("stakeholders", []))}

Release Strategy:
{planning.get("release_strategy", "")}

Success Metrics:
{format_list(planning.get("success_metrics", []))}
"""


def build_epic_description(project, epic):

    return f"""
{build_project_context(project)}


EPIC DETAILS

Description:
{epic.get("description", "")}

Business Objective:
{epic.get("business_objective", "")}

Business Value:
{epic.get("business_value", "")}

Priority:
{epic.get("priority", "")}

Owner:
{epic.get("owner", "")}

Estimated Duration:
{epic.get("estimated_duration", "")}

Scope:
{format_list(epic.get("scope", []))}

Out of Scope:
{format_list(epic.get("out_of_scope", []))}

Assumptions:
{format_list(epic.get("assumptions", []))}

Dependencies:
{format_list(epic.get("dependencies", []))}

Risks:
{format_list(epic.get("risks", []))}

Success Metrics:
{format_list(epic.get("success_metrics", []))}

Acceptance Criteria:
{format_list(epic.get("acceptance_criteria", []))}
"""


def build_feature_description(feature):

    return f"""
FEATURE DETAILS

Description:
{feature.get("description", "")}

Feature Type:
{feature.get("feature_type", "")}

Priority:
{feature.get("priority", "")}

Owner:
{feature.get("owner", "")}

Estimated Sprint:
{feature.get("estimated_sprint", "")}

Functional Requirements:
{format_list(feature.get("functional_requirements", []))}

Non-Functional Requirements:
{format_list(feature.get("non_functional_requirements", []))}

Technical Notes:
{feature.get("technical_notes", "")}

Dependencies:
{format_list(feature.get("dependencies", []))}

Business Rules:
{format_list(feature.get("business_rules", []))}

Acceptance Criteria:
{format_list(feature.get("acceptance_criteria", []))}
"""


def build_story_description(story):

    return f"""
USER STORY DETAILS

Detailed Description:
{story.get("detailed_description", "")}

As a:
{story.get("as_a", "")}

I want:
{story.get("i_want", "")}

So that:
{story.get("so_that", "")}

Priority:
{story.get("priority", "")}

Story Points:
{story.get("story_points", "")}

Estimated Effort:
{story.get("estimated_effort", "")}

Assigned Team:
{story.get("assigned_team", "")}

Labels:
{format_list(story.get("labels", []))}

Preconditions:
{format_list(story.get("preconditions", []))}

Postconditions:
{format_list(story.get("postconditions", []))}

Business Rules:
{format_list(story.get("business_rules", []))}

Acceptance Criteria:
{format_list(story.get("acceptance_criteria", []))}

Definition of Done:
{format_list(story.get("definition_of_done", []))}
"""


def build_task_description(task):

    return f"""
TASK DETAILS

Description:
{task.get("description", "")}

Task Type:
{task.get("task_type", "")}

Estimated Hours:
{task.get("estimated_hours", "")}

Owner:
{task.get("owner", "")}

Definition of Done:
{format_list(task.get("definition_of_done", []))}
"""


# ---------------------------------------------------------
# PUSH PROJECT
# ---------------------------------------------------------

def push_project(project):

    """
    Push nested backlog to Jira.

    Hierarchy:

    Epic
        ├── Feature
        ├── Story
        │      └── Subtasks
        └── Story

    Project-level Business Details and Scope & Planning
    are included in the Jira Epic description.
    """

    created = {
        "epics": [],
        "features": [],
        "stories": [],
        "tasks": []
    }

    print("\n========== PUSH PROJECT STARTED ==========\n")

    # -----------------------------------------------------
    # EPICS
    # -----------------------------------------------------

    for epic in project.get("epics", []):

        print(
            f"Creating Epic: {epic.get('title', 'Untitled Epic')}"
        )

        epic_description = build_epic_description(
            project,
            epic
        )

        epic_issue = client.create_issue(

            summary=epic.get(
                "title",
                "Untitled Epic"
            ),

            description=epic_description,

            issue_type="Epic"

        )

        epic_key = epic_issue["key"]

        created["epics"].append(
            epic_key
        )

        print(
            f"Created Epic -> {epic_key}"
        )

        # -------------------------------------------------
        # FEATURES
        # -------------------------------------------------

        for feature in epic.get(
            "features",
            []
        ):

            print(
                f"Creating Feature: "
                f"{feature.get('title', 'Untitled Feature')}"
            )

            feature_description = build_feature_description(
                feature
            )

            feature_issue = client.create_issue(

                summary=feature.get(
                    "title",
                    "Untitled Feature"
                ),

                description=feature_description,

                issue_type="Feature",

                parent_key=epic_key

            )

            feature_key = feature_issue["key"]

            created["features"].append(
                feature_key
            )

            print(
                f"Created Feature -> {feature_key}"
            )

            # ---------------------------------------------
            # STORIES
            # ---------------------------------------------

            for story in feature.get(
                "user_stories",
                []
            ):

                print(
                    f"Creating Story: "
                    f"{story.get('title', 'Untitled Story')}"
                )

                story_description = build_story_description(
                    story
                )

                story_issue = client.create_issue(

                    summary=story.get(
                        "title",
                        "Untitled Story"
                    ),

                    description=story_description,

                    issue_type="Story",

                    parent_key=epic_key

                )

                story_key = story_issue["key"]

                created["stories"].append(
                    story_key
                )

                print(
                    f"Created Story -> {story_key}"
                )

                # -----------------------------------------
                # TASKS
                # -----------------------------------------

                for task in story.get(
                    "tasks",
                    []
                ):

                    print(
                        f"Creating Task: "
                        f"{task.get('title', 'Untitled Task')}"
                    )

                    task_description = build_task_description(
                        task
                    )

                    task_issue = client.create_issue(

                        summary=task.get(
                            "title",
                            "Untitled Task"
                        ),

                        description=task_description,

                        issue_type="Subtask",

                        parent_key=story_key

                    )

                    task_key = task_issue["key"]

                    created["tasks"].append(
                        task_key
                    )

                    print(
                        f"Created Task -> {task_key}"
                    )

    print(
        "\n========== PUSH PROJECT FINISHED ==========\n"
    )

    print(
        json.dumps(
            created,
            indent=4
        )
    )

    return created