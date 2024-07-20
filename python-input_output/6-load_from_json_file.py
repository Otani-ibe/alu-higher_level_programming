#!/usr/bin/python3
"""
Provides functions for working with text files and JSON serialization.
"""


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python data structure represented by the JSON file content
    """
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
