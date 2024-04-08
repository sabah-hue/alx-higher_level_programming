"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv
if __name__ == "__main__":
    link = http://0.0.0.0:5000/search_user
    if argv[1]:
        data = {'q': argv[1]}
    else:
        data = {'q': ''}
