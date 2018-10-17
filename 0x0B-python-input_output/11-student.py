#!/usr/bin/python3


class Student:
    """create a new class"""
    def __init__(self, first_name, last_name, age):
        """initialize data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary representation"""
        return self.__dict__
