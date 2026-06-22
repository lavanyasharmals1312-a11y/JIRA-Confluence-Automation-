import json


def save_output(data, filepath):

    with open(filepath, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )