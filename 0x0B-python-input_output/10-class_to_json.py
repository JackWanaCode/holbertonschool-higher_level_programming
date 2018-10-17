#!/usr/bin/python3


def class_to_json(obj):
    """returns the dictionary description
    Args:
    obj: object
    Return: a dictionary format
    """
    return obj.__dict__
