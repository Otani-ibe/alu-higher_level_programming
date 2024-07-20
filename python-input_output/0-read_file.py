#!/usr/bin/python3
"""
This module provides a function to read a UTF-8 encoded text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The path to the text file. Default is an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        read_data = file.read()
        print(read_data, end='')
