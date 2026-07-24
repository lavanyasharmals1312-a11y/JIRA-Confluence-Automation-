def get_backlog_metrics(project):

    epics = len(project.get("epics", []))

    features = sum(
        len(epic.get("features", []))
        for epic in project.get("epics", [])
    )

    stories = sum(
        len(feature.get("user_stories", []))
        for epic in project.get("epics", [])
        for feature in epic.get("features", [])
    )

    tasks = sum(
        len(story.get("tasks", []))
        for epic in project.get("epics", [])
        for feature in epic.get("features", [])
        for story in feature.get("user_stories", [])
    )

    return epics, features, stories, tasks