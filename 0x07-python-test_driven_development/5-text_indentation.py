#!/usr/bin/python3

"""Print a paragraph
Args:
size: size of square
Returns: nothing"""

def text_indentation(text):
    """print paragraph and give space after ".?:"
    """
    l_text = []
    check = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for c in text:
            if c in "?.:":
                l_text += c + "\n\n"
                check = 1
            elif c == " " and check == 1:
                l_text += ""
                check = 0
            else:
                l_text += c
        print("".join(l_text), end="")
