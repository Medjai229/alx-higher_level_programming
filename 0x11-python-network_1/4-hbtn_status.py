#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from requests import get


if __name__ == "__main__":
    body = get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
