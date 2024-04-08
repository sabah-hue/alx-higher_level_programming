#!/usr/bin/python3
""" sends a request to the URL """
import urllib.request
from sys import argv
if __name__ == "__main__":
    link = argv[1]
    req = urllib.request.Request(link)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
