#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square.
            size (int): The size of the new square.
        """
        self.__size = size

    def size(self):
        """get the current size of the square"""
        return (self.__size)

    def size(self, value):
        """set a new size for the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size ** 2)
