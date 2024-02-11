#!/usr/bin/python3
"""Base Class."""
from json import dumps, loads


class Base:
    """the “base” of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the base object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts."""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
