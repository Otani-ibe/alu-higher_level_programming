#!/usr/bin/python3
"""
Provides functions to read, write, and append to UTF-8 text files.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns the number of characters added.

    Args:
        filename (str): The path to the text file. Default is an empty string.
        text (str): The string to append to the text file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
