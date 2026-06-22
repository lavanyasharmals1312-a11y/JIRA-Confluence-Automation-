from datetime import datetime


def build_project_schema(project_name):

    return {
        "project_name": project_name,
        "generated_at": str(datetime.now()),
        "epics": []
    }