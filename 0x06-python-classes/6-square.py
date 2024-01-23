#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (not isinstance(position[0], int) or
                not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            sefl.__position = position

    def area(self):
        """Return the current area of the square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set a new size for the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property to retrieve it"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """property setter to set it"""
        self.__position = value

    def my_print(self):
        """print the square with '#'"""
        if self.__size == 0:
            print("")
            return

        if self.__position[1] > 0:
            for p in range(0, self.__position[1]):
                print("")

        for i in range(self.__size):
            if self.__position[0] > 0:
                for x in range(self.__position[0]):
                    print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
