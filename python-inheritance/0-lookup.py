#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of attributes and methods of an object.

    Args:
    obj (object): The object to inspect.

    Returns:
    list: List of strings representing attributes and methods of the object.
    """
    return dir(obj)
