#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""
import requests
if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(link).text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
