#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """new sub class"""
    def __init__(self, size):
        """initialize data"""
        super().__init__(size, size)
