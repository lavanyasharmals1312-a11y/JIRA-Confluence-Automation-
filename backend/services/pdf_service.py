from pathlib import Path

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


OUTPUT_FOLDER = (
    Path(__file__).resolve().parents[1] / "outputs"
)


styles = getSampleStyleSheet()


def heading(text):

    return Paragraph(

        f"<b>{text}</b>",

        styles["Heading2"]

    )


def normal(text):

    return Paragraph(

        str(text),

        styles["BodyText"]

    )


def generate_pdf(project):

    filename = (
        OUTPUT_FOLDER
        /
        f"{project['project_name'].replace(' ','_')}.pdf"
    )

    doc = SimpleDocTemplate(
        str(filename)
    )

    story = []

    story.append(

        Paragraph(

            project["project_name"],

            styles["Title"]

        )

    )

    story.append(

        Spacer(1,20)

    )

    story.append(

        heading("Project Description")

    )

    story.append(

        normal(

            project.get(
                "project_description",
                ""
            )

        )

    )

    story.append(

        Spacer(1,12)

    )

    if "executive_summary" in project:

        story.append(

            heading(
                "Executive Summary"
            )

        )

        summary = project["executive_summary"]

        if isinstance(summary, dict):

            for key, value in summary.items():

                story.append(

                    heading(

                        key.replace(
                            "_",
                            " "
                        ).title()

                    )

                )

                if isinstance(value, list):

                    for item in value:

                        story.append(

                            normal(
                                "• " + item
                            )

                        )

                else:

                    story.append(

                        normal(value)

                    )

        else:

            story.append(

                normal(summary)

            )

    story.append(

        Spacer(1,20)

    )

    for epic in project.get(
        "epics",
        []
    ):

        story.append(

            heading(

                f"{epic['epic_id']} - {epic['title']}"

            )

        )

        story.append(

            normal(
                epic.get(
                    "description",
                    ""
                )
            )

        )

        story.append(

            normal(
                f"Business Objective: {epic.get('business_objective','')}"
            )

        )

        story.append(

            normal(
                f"Business Value: {epic.get('business_value','')}"
            )

        )

        story.append(

            Spacer(1,12)

        )

        for feature in epic.get(
            "features",
            []
        ):

            story.append(

                heading(

                    f"{feature['feature_id']} - {feature['title']}"

                )

            )

            story.append(

                normal(
                    feature.get(
                        "description",
                        ""
                    )
                )

            )

            for story_item in feature.get(
                "user_stories",
                []
            ):

                story.append(

                    heading(

                        f"{story_item['story_id']} - {story_item['title']}"

                    )

                )

                story.append(

                    normal(
                        story_item.get(
                            "description",
                            ""
                        )
                    )

                )

                for task in story_item.get(
                    "tasks",
                    []
                ):

                    story.append(

                        normal(

                            f"{task['task_id']} - {task['title']}"

                        )

                    )

    doc.build(
        story
    )

    return filename