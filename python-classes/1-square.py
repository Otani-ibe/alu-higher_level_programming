#!/usr/bin/python3
"""
Square Module

This module defines the Square class for representing squares.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
    __size (int): Private attribute representing the size of the square.
    """

    def __init__(self, size):
    """
        Initializes a Square instance.

        Parameters:
        size (int): The size of the square.

        Returns:
        None
     """
        self.__size = size
