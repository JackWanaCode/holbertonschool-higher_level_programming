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
        try:
            if value < 0:
                int("dog")
            self.__size = value
        except TypeError:
            raise Exception("size must be an integer")
        except ValueError:
            raise Exception("size must be >= 0")

    def area(self):
        """calculate area of square"""
        return self.__size * self.__size

    def my_print(self):
        """"print square with #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
