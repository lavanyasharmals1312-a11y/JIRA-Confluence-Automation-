from ai_engine.parser import load_requirement
from ai_engine.generator import generate_backlog

with open(
    "prompts/master_prompt.txt",
    "r",
    encoding="utf-8"
) as f:
    prompt = f.read()

requirement = load_requirement(
    "sample_docs/crm_requirements.txt"
)

result = generate_backlog(
    prompt,
    requirement
)

with open(
    "outputs/generated_backlog.json",
    "w",
    encoding="utf-8"
) as f:
    f.write(result)

print("Backlog saved successfully.")