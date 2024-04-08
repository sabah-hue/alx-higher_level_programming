#!/usr/bin/python3
""" sends a POST request to the passed URL """
import requests
from sys import argv
if __name__ == "__main__":
    link = argv[1]
    payload = {'email': argv[2]}
    r = requests.post(link, data=payload).text
    print(r)
