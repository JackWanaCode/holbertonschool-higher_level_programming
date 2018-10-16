#!/usr/bin/python3


class MyInt(int):
    """compare to interger"""
    def __init__(self, value):
        """initialize attribute"""
        self.value = value

    def __str__(self):
        """print the value"""
        return str(self.value)

    def __eq__(self, other):
        """compare two integer"""
        return self.value == other
