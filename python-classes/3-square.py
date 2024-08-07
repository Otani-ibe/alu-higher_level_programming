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

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Parameters:
        size (int, optional): The size of the square (default is 0).

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

        Returns:
        None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2
