#!/usr/bin/python3
"""
This module provides a function to write a string to a UTF-8 encoded text
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters

    Args:
        filename (str): The path to the text file. Default is an empty string.
        text (str): The string to write to the text file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
