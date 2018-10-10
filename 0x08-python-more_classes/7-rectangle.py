#!/usr/bin/python3
class Rectangle:
    """make a new class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize class attributes"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = value

    def area(self):
        """calculate area of shape"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter of shape"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """print a square of '#'"""
        lis = []

        for i in range(self.height):
            if self.width > 0:
                lis += [str(self.print_symbol) * self.width]
        return "\n".join(lis)

    def __repr__(self):
        """print repr"""
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """delete a instance"""
        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
