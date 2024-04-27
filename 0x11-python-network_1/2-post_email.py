#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response
"""
from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")

    with urlopen(argv[1], data) as response:
        print(response.read().decode("utf-8"))
