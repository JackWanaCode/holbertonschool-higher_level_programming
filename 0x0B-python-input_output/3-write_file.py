#!/usr/bin/python3
def write_file(filename="", text=""):
    """read n lines of a text file
    Args:
    filename: name of file
    text: content will be wrote into the file
    Return: number of charaters added
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
