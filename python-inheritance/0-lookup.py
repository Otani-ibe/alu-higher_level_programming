#!/usr/bin/python3
"""
This is a sample module that demonstrates module, class, and function.

Classes:
- MyClass: A sample class demonstrating attributes and methods.  
Functions:
- lookup(obj): Returns a list of available attributes and methods of an object.
"""


class MyClass:
    """
    This is a sample class.

    Attributes:
    - data: A sample attribute storing some data.

    Methods:
    - method(): A sample method returning a string.
    """

    def __init__(self):
        self.data = "example data"    
    def method(self):
        """
        A sample method returning a string.

        Returns:
        - str: A fixed string indicating method completion.
        """
        return "example method"


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    - obj: Any Python object

    Returns:
    - List of strings: Names of attributes and methods of the object
    """
    return dir(obj)
