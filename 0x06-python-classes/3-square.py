#!/usr/bin/python3
class Square:
    """create Square class"""
    def __init__(self, size=0):
        """initialize the data."""
        self.__size = size
        try:
            if size < 0:
                int("dog")
        except TypeError:
            raise Exception("size must be an integer")
        except ValueError:
            raise Exception("size must be >= 0")

    def area(self):
        """calculate area of square"""
        return self.__size * self.__size
