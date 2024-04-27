#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
from requests import post


if __name__ == "__main__":
    value = {"q": "" if len(argv) < 2 else argv[1]}
    res = post("http://0.0.0.0:5000/search_user", data=value)

    try:
        response = res.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
