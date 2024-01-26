#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repository_name}/commits'

    # Fetch the commit data from the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        commits = response.json()

        # Display the 10 most recent commits
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")

    else:
        print(f"Error: Unable to fetch commits. Status Code: {response.status_code}")
