#!/usr/bin/python3
"""
Provides functions for working with text files and JSON serialization/deserialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    (list, dictionary, string, integer, and boolean) for JSON serialization

    Args:
        obj: The object instance to be serialized.

    Returns:
        dict: The dictionary description of the object for JSON serialization.
    """
    return obj.__dict__
