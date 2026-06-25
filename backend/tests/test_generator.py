from pathlib import Path

from backend.ai_engine.prompt_loader import (
    load_prompt
)

from backend.ai_engine.generator import (
    generate_backlog
)

from backend.parsers.txt_parser import (
    extract_text
)

from backend.storage.save_project import (
    save_project
)


sample = (
    Path(__file__).resolve().parents[1]
    / "sample_docs"
    / "crm_requirements.txt"
)

requirement = extract_text(sample)

prompt = load_prompt(
    "master_prompt.txt"
)

project = generate_backlog(

    prompt,

    requirement
)

save_project(project)

print("Project generated successfully.")