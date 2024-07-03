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

        Returns:
        None
        """
        self.width = width
        self.height = height
