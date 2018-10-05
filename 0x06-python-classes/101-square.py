#!/usr/bin/python3
class Square:
    """create Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the data."""
        self.size = size
        self.position = position

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
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """calculate area of square"""
        return self.size * self.size

    def __str__(self):
        """"make as string that have square with #"""
        string = []
        if self.position[1] > 0 and self.size > 0:
            string += ["\n" * (self.position[1])]
        for i in range(self.size):
            if self.position[0] > 0:
                string += [" " * self.position[0]]
            string += ["#" * self.size]
            if i < self.size - 1:
                string += ["\n"]
        return "".join(string)
