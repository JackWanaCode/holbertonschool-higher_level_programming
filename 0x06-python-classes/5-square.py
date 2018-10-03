#!/usr/bin/python3
class Square:
    """create Square class"""
    def __init__(self, size=0):
        """initialize the data."""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        elif value != int(value):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    def area(self):
        """calculate area of square"""
        return self.__size * self.__size

    def my_print(self):
        """"print square with #"""
        for i in range(self.__size):
            print("#" * self.__size, end="")
            print("")
        if self.__size == 0:
            print("")
