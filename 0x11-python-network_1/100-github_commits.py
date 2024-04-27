#!/usr/bin/python3
"""
Python script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    response = get("https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1]))
    commits = response.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
