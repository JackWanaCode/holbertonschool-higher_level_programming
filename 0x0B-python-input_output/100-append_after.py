#!/usr/bin/python3


def append_after(filename="", search_string="", new_string=""):
    """append a new string to file
    Args:
    filename: file that will be added
    search_string: string to be matched
    new_string: string to be added
    Return: nothing
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if search_string in line:
                f.write(line)
                f.write(new_string)
            else:
                f.write(line)
