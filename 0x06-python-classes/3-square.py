#!/usr/bin/python3
class Square:
    """create Square class"""
    def __init__(self, size=0):
        """initialize the data."""
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        elif size != int(size):
            raise TypeError("size must be an integer")

    def area(self):
        """calculate area of square"""
        return self.__size * self.__size
