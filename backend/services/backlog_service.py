from backend.ai_engine.prompt_loader import load_prompt

from backend.ai_engine.generator import (
    generate_backlog
)

from backend.storage.save_project import (
    save_project
)


def generate_project(
    requirement,
    provider,
    project_name
):
    """
    Complete backlog generation pipeline.
    """

    # -------------------------------
    # Load Master Prompt
    # -------------------------------

    prompt = load_prompt(
        "master_prompt.txt"
    )

    # -------------------------------
    # Generate Backlog
    # -------------------------------

    project = generate_backlog(

        prompt=prompt,

        requirement=requirement,

        provider_name=provider

    )
    print("\n==================== PROJECT ====================")
    print(type(project))
    print(project)
    print("=================================================\n")

    # -------------------------------
    # Override project name
    # -------------------------------

    # --------------------------------
    # Ensure project metadata exists
    # --------------------------------

    if not isinstance(project, dict):
        raise ValueError("AI did not return a valid JSON object.")

    project.setdefault("project_name", "")

    if project_name.strip():
        project["project_name"] = project_name
    elif not project["project_name"]:
        project["project_name"] = "Untitled Project"

    # -------------------------------
    # Save Project
    # -------------------------------

    filepath = save_project(project)

    return project, filepath