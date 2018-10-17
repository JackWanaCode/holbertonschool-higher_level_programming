#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """return the JSON presention of an object
    Args:
    my_obj: object
    Return: JSON presentation
    """
    return json.dumps(my_obj, sort_keys=True)
