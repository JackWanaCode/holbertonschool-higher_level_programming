#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """read n lines of a text file
    Args:
    filename: name of file
    nb_lines: number of line will be printed
    Return: content of line(s)
    """
    i = 1
    with open(filename, 'r') as f:
        for line in f:
            if i <= nb_lines or nb_lines < 1:
                print(line, end='')
                i += 1
