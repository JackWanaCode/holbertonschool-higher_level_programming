#!/usr/bin/python3


def add_attribute(obj, key, value):
    if '__dict__' in dir(obj):
        obj.__dict__[key] = value
    else:
        raise TypeError("can't add new attribute")
