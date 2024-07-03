#!/usr/bin/python3
"""
Rectangle Module

This module defines the Rectangle class for representing rectangles.
"""


class Rectangle:
    """
    A class that defines a rectangle.

    Attributes:
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.

        Parameters:
        width (int, optional): Width of the rectangle (default is 0).
        height (int, optional): Height of the rectangle (default is 0).

        Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.

        Returns:
        None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:
        value (int): The width to set.

        Raises:
        TypeError: If width is not an integer.
        ValueError: If width is less than 0.

        Returns:
        None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
        int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters:
        value (int): The height to set.

        Raises:
        TypeError: If height is not an integer.
        ValueError: If height is less than 0.

        Returns:
        None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#'.

        Returns:
        str: String representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.strip()

    def __repr__(self):
        """
    Returns a string representation of the rectangle for debugging purposes.

     Returns:
        str: String representation of the rectangle.
        """
        return f"<{self.__class__.__name__}(width={self.width}, height={self.height})>"
