#!/usr/bin/python3
def append_write(filename="", text=""):
    """read n lines of a text file
    Args:
    filename: name of file
    text: content will be wrote into the file
    Return: number of charaters added
    """
    with open(filename, 'a') as f:
        return f.write(text)
