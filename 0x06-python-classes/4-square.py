#!/usr/bin/python3
class Square:
    """create Square class"""
    def __init__(self, size=0):
        """initialize the data."""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate area of square"""
        return self.__size * self.__size
