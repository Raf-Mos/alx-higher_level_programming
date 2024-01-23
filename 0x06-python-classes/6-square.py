#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not type(position) is tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not type(position[0]) is int) or (not type(position[1]) is int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set size"""
        self.__size = value

    @property
    def position(self):
        """property to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter to set position"""
        self.__position = value

    def area(self):
        """Public instance that returns the  square area"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance that prints the square with the char #"""
        if self.__size == 0:
            print("")
            return
        if self.__position[1] > 0:
            for p in range(0, self.__position[1]):
                print("")
        for i in range(0, self.__size):
            if self.__position[0] > 0:
                for k in range(0, self.__position[0]):
                    print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
