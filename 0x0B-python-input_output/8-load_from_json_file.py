#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """return created Object from a “JSON file”
    Args:
    filename: name of file to be load
    Return: nothing
    """
    with open(filename, 'r') as f:
        return json.load(f)
