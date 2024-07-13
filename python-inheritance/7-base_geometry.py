#!/usr/bin/python3
"""
Module: base_geometry

This module defines the BaseGeometry class.

Classes:
- BaseGeometry: A class with methods for calculating area integers
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
