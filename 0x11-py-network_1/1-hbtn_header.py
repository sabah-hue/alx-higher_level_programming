#!/usr/bin/python3
"""  sends a request to the URL  """
import urllib.request
from sys import argv
if __name__ == "__main__":
    link = argv[1]
    with urllib.request.urlopen(link) as response:
        html = response.headers
        print(html.get('X-Request-Id'))
