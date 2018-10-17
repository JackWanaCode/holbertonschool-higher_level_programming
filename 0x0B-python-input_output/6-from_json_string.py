#!/usr/bin/python3
import json


def from_json_string(my_str):
    """return the JSON presention of an object
    Args:
    my_obj: object
    Return: JSON presentation
    """
    return json.dumps(json.loads(my_str), sort_keys=True)
