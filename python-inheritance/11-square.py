#!/usr/bin/python3
"""
Module: square

This module defines the Square class that inherits from Rectangle.

Author: [Your Name]

Classes:
- Rectangle: A class representing a rectangle.
- Square: A class representing a square, inherits from Rectangle.
"""


class BaseGeometry:
    """
    A class with methods for calculating area and validating integers.
    """

    def area(self):
        """
        Raises an exception indicating that the area method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0.

        Args:
        - name: A string representing the name of the parameter.
        - value: The value to validate.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
    - width: The width of the rectangle.
    - height: The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with width and height.

        Args:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
        - str: The string representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculates the area of the Rectangle.

        Returns:
        - int: The area of the Rectangle.
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    A class representing a square, inherits from Rectangle.

    Attributes:
    - size: The size of the square (private).

    Methods:
    - area(): Returns the area of the square.
    - __str__(): Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a Square with size.

        Args:
        - size: The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
        - str: The string representation of the Square.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        Calculates the area of the Square.

        Returns:
        - int: The area of the Square.
        """
        return self.__size ** 2
