#!/usr/bin/python3
"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""
from sys import argv
from requests import get, auth


if __name__ == "__main__":
    basic_auth = auth.HTTPBasicAuth(argv[1], argv[2])
    response = get("https://api.github.com/user", auth=basic_auth)
    print(response.json().get("id"))
