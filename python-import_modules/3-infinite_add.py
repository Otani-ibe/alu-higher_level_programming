#!/usr/bin/python3
import sys
if __name__ == "__main__":

    # Get the command line arguments
    args = sys.argv[1:]

    # Convert arguments to integers and calculate their sum
    total = sum(int(arg) for arg in args)

    # Print the result
    print(total)
