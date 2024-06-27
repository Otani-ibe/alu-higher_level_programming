#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if 0 <= idx < len(my_list):
        return my_list

    # Modify the list by replacing the element at idx with the new element
    my_list[idx] = element
