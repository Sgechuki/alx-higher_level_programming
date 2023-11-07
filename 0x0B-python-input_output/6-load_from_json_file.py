#!/usr/bin/python3
"""Module holds only one function,
def load_from_json_file(filename)"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename) as f:
        return json.loads(f.read())
