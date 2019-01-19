#!/usr/bin/python3

class Binary_Node:
    """create Node class"""
    def __init__(self, number, parent_node=None, left_node=None, right_node=None):
        self.number = number
        self.parent_node = parent_node
        self.left_node = left_node
        self.right_node = right_node

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) is not int:
            raise TypeError("value must be integer")
        else:
            self.__number = value
