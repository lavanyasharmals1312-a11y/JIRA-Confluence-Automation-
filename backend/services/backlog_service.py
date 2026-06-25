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

    # -------------------------------
    # Override project name
    # -------------------------------

    if project_name.strip():

        project["project_name"] = project_name

    # -------------------------------
    # Save Project
    # -------------------------------

    save_project(project)

    return project