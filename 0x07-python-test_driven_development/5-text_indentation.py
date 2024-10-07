#!/usr/bin/python3
"""
Contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
No space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines
    after each of these characters: ., ? and :
    text is a string, otherwise raise a TypeError exception:
    "text must be a string"
    No space at the beginning or at the end of each printed line
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ('.', ':', '?'):
            print("{}".format(text[i]))
            print("")
            if text[i + 1] == " ":
                i += 2
            else:
                i += 1
        else:
            print("{}".format(text[i]), end="")
            i += 1
    print("")
