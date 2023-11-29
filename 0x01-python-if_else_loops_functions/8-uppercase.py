#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        c = ord(letter)
        if c in range(97, 123):
            c = c - 32
        print("{:c}".format(c), end="")
    print()
