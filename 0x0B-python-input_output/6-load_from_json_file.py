#!/usr/bin/python3
""" module ..."""
import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
