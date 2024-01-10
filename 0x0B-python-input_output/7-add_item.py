#!/usr/bin/python3
""" module ..."""
from sys import argv


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

def adds():
    """add args to list """
    try:
        items = load('add_item.json')
        save(items + argv[1:], 'add_item.json')
    except Exception:
        save(argv[1:], 'add_item.json')

if __name__ == "__main__":
    adds()
