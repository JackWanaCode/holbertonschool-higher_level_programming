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
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] >= 0 or value[1] >= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculate area of square"""
        return self.__size * self.__size

    def my_print(self):
        """"print square with #"""
        print(self.__size)
        if self.__position[1] > 0:
            print("\n" * (self.__position[1] - 1))
        for i in range(self.__size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print("")
        if self.__size == 0:
            print("")
