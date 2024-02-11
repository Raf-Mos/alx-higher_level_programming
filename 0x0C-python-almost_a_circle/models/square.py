#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Construtor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string info about the Square"""
        return '[{}] ({}) {}/{} - {}'.format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """The size property."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method to update the Square"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def __update(self, id=None, size=None, x=None, y=None):
        """update attributes via *args and **kwargs"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
