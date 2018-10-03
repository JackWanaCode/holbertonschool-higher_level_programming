#!/usr/bin/python3
class Square:
    """create Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the data."""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        try:
            if value[0] < 0 or value[1] < 0:
                int("dog")
        except (TypeError, ValueError):
            raise Exception("position must be a tuple of 2 positive integers")

    def area(self):
        """calculate area of square"""
        return self.__size * self.__size

    def my_print(self):
        """"print square with #"""
        if self.__position[1] > 0:
            print("\n" * (self.__position[1] - 1))
        for i in range(self.__size):
            if self.__position[0] > 0:
                print("_" * self.__position[0], end="")
            print("#" * self.__size, end="")
            print("")
        if self.__size == 0:
            print("")
