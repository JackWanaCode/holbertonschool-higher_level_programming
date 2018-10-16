#!/usr/bin/python3


class BaseGeometry:
    """create a new class"""
    def area(self):
        """function to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating the input data"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value

class Rectangle(BaseGeometry):
    """new sub class"""
    def __init__(self, width, height):
        """initilialize the data"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
