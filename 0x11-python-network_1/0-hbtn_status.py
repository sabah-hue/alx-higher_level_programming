#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request
if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(link) as response:
        html = response.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode())
