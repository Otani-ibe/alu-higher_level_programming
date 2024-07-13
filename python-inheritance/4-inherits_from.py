#!/usr/bin/python3
"""
Module: inheritance_check

This module provides a function to check if an obj is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited from class

    Args:
    - obj: Any Python object.
    - a_class: The class to check against.

    Returns:
    - bool: True if obj is an instance of a class that inherited from a_class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
