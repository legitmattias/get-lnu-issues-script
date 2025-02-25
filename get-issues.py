import requests

TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with your actual GitLab token
PROJECT_ID = "YOUR_PROJECT_ID"  # Replace with the actual project ID
URL = f"https://gitlab.lnu.se/api/v4/projects/{PROJECT_ID}/issues?sort=asc"

headers = {"PRIVATE-TOKEN": TOKEN}
response = requests.get(URL, headers=headers)

if response.status_code == 200:
    issues = response.json()
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
    print("Failed to fetch issues:", response.status_code)

