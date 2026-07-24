import requests

from backend.integrations.auth import (
    get_jira_credentials
)


class JiraClient:

    def __init__(self, creds=None):

        if creds is None:
            creds = get_jira_credentials()

        self.base_url = creds["base_url"]
        self.email = creds["email"]
        self.api_token = creds["api_token"]
        self.project_key = creds["project_key"]

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        self.auth = (
            self.email,
            self.api_token
        )

    # -------------------------------------------------
    # Convert plain text to Jira Document Format (ADF)
    # -------------------------------------------------

    def build_adf(self, text):

        content = []

        for line in text.split("\n"):

            line = line.strip()

            if not line:
                continue

            # Bullet list
            if line.startswith("•"):

                content.append({

                    "type": "bulletList",

                    "content": [

                        {

                            "type": "listItem",

                            "content": [

                                {

                                    "type": "paragraph",

                                    "content": [

                                        {

                                            "type": "text",

                                            "text": line[1:].strip()

                                        }

                                    ]

                                }

                            ]

                        }

                    ]

                })

            else:

                content.append({

                    "type": "paragraph",

                    "content": [

                        {

                            "type": "text",

                            "text": line

                        }

                    ]

                })

        return {

            "type": "doc",

            "version": 1,

            "content": content

        }

    # -------------------------------------------------
    # Test Connection
    # -------------------------------------------------

    def test_connection(self):

        url = f"{self.base_url}/rest/api/3/myself"

        response = requests.get(

            url,

            headers=self.headers,

            auth=self.auth

        )

        if response.status_code == 200:

            return True, response.json()

        return False, response.text

    # -------------------------------------------------
    # Get Project
    # -------------------------------------------------

    def get_project(self):

        url = f"{self.base_url}/rest/api/3/project/{self.project_key}"

        response = requests.get(

            url,

            headers=self.headers,

            auth=self.auth

        )

        if response.status_code == 200:

            return response.json()

        raise Exception(response.text)

    # -------------------------------------------------
    # Create Issue
    # -------------------------------------------------

    def create_issue(

        self,

        summary,

        description,

        issue_type,

        parent_key=None

    ):

        url = f"{self.base_url}/rest/api/3/issue"

        fields = {

            "project": {

                "key": self.project_key

            },

            "summary": summary,

            "issuetype": {

                "name": issue_type

            },

            "description": self.build_adf(description)

        }

        if parent_key is not None:

            fields["parent"] = {

                "key": parent_key

            }

        payload = {

            "fields": fields

        }

        response = requests.post(

            url,

            json=payload,

            headers=self.headers,

            auth=self.auth

        )

        if response.status_code in [200, 201]:

            return response.json()

        raise Exception(response.text)
    
        raise Exception(response.text)

    # -------------------------------------------------
    # Get Create Metadata
    # -------------------------------------------------

    def get_create_metadata(self):

        url = (
            f"{self.base_url}/rest/api/3/issue/createmeta"
            f"?projectKeys={self.project_key}&expand=projects.issuetypes"
        )

        response = requests.get(
            url,
            headers=self.headers,
            auth=self.auth
        )

        print("Status:", response.status_code)
        print(response.text)

        return response.json()