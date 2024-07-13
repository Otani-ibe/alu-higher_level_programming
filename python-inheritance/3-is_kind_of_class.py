#!/usr/bin/python3
"""
Module: type_check

This module provides a function to check if an object is an instance of.

Functions:
- is_kind_of_class(obj, a_class): Returns True if the object is an instance
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of.

    Args:
    - obj: Any Python object.
    - a_class: The class to check against.

    Returns:
    - bool: True if obj is an instance of a_class or a subclass of a_class.
    """
    return isinstance(obj, a_class)
