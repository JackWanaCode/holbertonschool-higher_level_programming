#!/usr/bin/python3


class Student:
    """create a new class"""
    def __init__(self, first_name, last_name, age):
        """initialize data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation"""
        dic = {}
        if type(attrs) is not list:
            dic = self.__dict__
        else:
            for k, v in self.__dict__.items():
                if k in attrs:
                    dic[k] = v
        return dic
