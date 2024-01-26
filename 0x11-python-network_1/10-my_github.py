#!/usr/bin/python3
"""Uses GitHub API to display user id"""

import requests
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'

    # Set up basic authentication using personal access token
    auth = (username, token)

    response = requests.get(url, auth=auth)

    try:
        data = response.json()
        user_id = data.get('id')
        print(user_id)
    except ValueError:
        print("None")
