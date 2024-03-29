#!/usr/bin/python3
""" sends a request to the URL and displays
the value of the variable X-Request-Id """
import requests
from sys import argv
if __name__ == "__main__":
    link = argv[1]
    r = requests.get(link).headers.get('X-Request-Id')
    print(r)
