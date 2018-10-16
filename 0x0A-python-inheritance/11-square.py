#!/usr/bin/python3


class BaseGeometry:
    """create a new class"""
    def area(self):
        """calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating input data"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value


class Rectangle(BaseGeometry):
    """new sub class"""
    def __init__(self, width, height):
        """initialize the data"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def __str__(self):
        """return str function"""
        w = str(self.__width)
        h = str(self.__height)
        name = str(self.__class__.__name__)
        lis = ["["] + [name] + ["] "] + [w] + ["/"] + [h]
        return "".join(lis)

    def area(self):
        """overwrite area function"""
        return self.__width * self.__height


class Square(Rectangle):
    """new sub class"""
    def __init__(self, size):
        """initialize data"""
        super().__init__(size, size)
