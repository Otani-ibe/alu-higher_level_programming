#!/usr/bin/python3
"""
Module: my_list

This module defines the MyList class, a subclass of list with additional functionalities.

Classes:
- MyList: A subclass of list that adds sorting capabilities.

Public Methods:
- print_sorted(): Prints the list in ascending order.
"""


class MyList(list):
    """
    A subclass of list that adds sorting capabilities.

    Methods:
    - print_sorted(): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
