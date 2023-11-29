#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) in range(97, 123):
            print("{:c}".format(ord(letter) - 32), end="")
    print()
