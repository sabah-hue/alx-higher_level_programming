#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response """
import requests
from sys import argv
if __name__ == "__main__":
    link = argv[1]
    try:
        r = requests.get(link)
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
