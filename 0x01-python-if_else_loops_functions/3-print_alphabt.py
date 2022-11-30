#!/usr/bin/python3

"""A Program that prints the ASCII alphabet, in lowercase
    except 'q' and 'e'
"""

for character in range(97, 123):
    if character != 101 and character != 113:
        print("{}".format(chr(character)), end="")
