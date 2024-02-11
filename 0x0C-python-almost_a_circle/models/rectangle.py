#!/usr/bin/python3
"""Module for Rectangle class."""
from modules.base import Base


class Rectangle(Base):
    """A Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The width property."""
        return self.__width
    @width.setter
    def width(self, value):
        self.validate_att("width", value, False)
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height
    @height.setter
    def height(self, value):
        self.validate_att("height", value, False)
        self.__height = value

    @property
    def x(self):
        """The x property."""
        return self.__x
    @x.setter
    def x(self, value):
        self.validate_att("x", value)
        self.__x = value

    @property
    def y(self):
        """The y property."""
        return self.__y
    @y.setter
    def y(self, value):
        self.validate_att("y", value)
        self.__y = value

    def validate_att(self, name, value, eq_zero=True):
        """Method to check the attributes"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq_zero and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq_zero and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """area of the Rectangle"""
        return self.height * self.width

    def display(self):
        """Print the Rectangle using the `#` character."""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """Returns string info about the Rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y,
                   self.width, self.height)
