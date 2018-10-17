#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """return the JSON presention of an object
    Args:
    my_obj: object
    filename: name of file to be saved
    Return: JSON presentation
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f, sort_keys=True)
