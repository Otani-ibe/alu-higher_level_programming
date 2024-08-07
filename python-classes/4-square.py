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
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Parameters:
        value (int): The size to set.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

        Returns:
        None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2
