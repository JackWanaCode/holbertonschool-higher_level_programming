#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except ZeroDivisionError as ze:
        print("Exception:", ze, file=sys.stderr)
        return None
    except IndexError as ie:
        print("Exception:", ie, file=sys.stderr)
        return None
