#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    response = get(argv[1])
    code = response.status_code

    if code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(code))
