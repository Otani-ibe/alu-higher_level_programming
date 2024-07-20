#!/usr/bin/python3
"""
Provides functions for working with text files and JSON serialization.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized to a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
