import requests
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("GITLAB_TOKEN")  # Loaded from .env
PROJECT_ID = os.getenv("GITLAB_PROJECT_ID")  # Loaded from .env
PROJECT_URL = f"https://gitlab.lnu.se/api/v4/projects/{PROJECT_ID}"
ISSUES_URL = f"https://gitlab.lnu.se/api/v4/projects/{PROJECT_ID}/issues?sort=asc"

headers = {"PRIVATE-TOKEN": TOKEN}

# Fetch project details
project_response = requests.get(PROJECT_URL, headers=headers)

if project_response.status_code == 200:
    project_name = project_response.json().get("name", "Unknown Project")
    print(f"# {project_name}\n")
else:
    print("Failed to fetch project details:", project_response.status_code)
    exit(1)

# Fetch issues
issues_response = requests.get(ISSUES_URL, headers=headers)

if issues_response.status_code == 200:
    issues = issues_response.json()
    for issue in issues:
        issue_number = issue['iid']
        title = issue['title']
        state = issue['state']
        description = issue['description'] or "No description provided."
        labels = issue.get('labels', [])

        print(f"## Issue {issue_number}: {title}\n")
        print(f"**Status:** {state}\n")
        print(f"{description}\n")
        
        if labels:
            print("**Labels:**")
            for label in labels:
                print(f"- {label}")
        else:
            print("_No labels assigned._")

        print("\n---\n")
else:
    print("Failed to fetch issues:", issues_response.status_code)
