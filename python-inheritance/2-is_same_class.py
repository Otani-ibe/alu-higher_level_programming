#!/usr/bin/python3
"""
Module: type_check

This module provides a function to check if an object is instance of class

Functions:
- is_same_class(obj, a_class
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
    - obj: Any Python object.
    - a_class: The class to check against.

    Returns:
    - bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
