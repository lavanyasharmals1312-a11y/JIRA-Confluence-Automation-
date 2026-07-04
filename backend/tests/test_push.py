import json

from backend.storage.latest_project_path import (
    latest_project_path
)

from backend.services.jira_service import (
    push_project
)

filepath = latest_project_path()

with open(

    filepath,

    "r",

    encoding="utf-8"

) as f:

    project = json.load(f)

result = push_project(project)

print(result)