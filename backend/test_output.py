from ai_engine.schema_builder import build_project_schema
from ai_engine.storage import save_output

project = build_project_schema(
    "CRM Project"
)

save_output(
    project,
    "outputs/project_001.json"
)

print("Saved Successfully")