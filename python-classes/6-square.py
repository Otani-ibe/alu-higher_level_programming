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
__position (tuple): Private attribute representing the position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with an optional size and position.

        Parameters
        size(int, optional): The size of the square (default = 0)
        position(tuple, optional):The position of the square(default = (0, 0))

        Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0.

        Returns:
        None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
        tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Parameters:
        value (tuple): The position to set.

        Raises:
        TypeError: If position is not a tuple of 2 positive integers.

        Returns:
        None
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #.

        If the size is equal to 0, prints an empty line.
        Position is used to adjust the printing location.

        Returns:
        None
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
