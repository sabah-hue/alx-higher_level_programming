#!/usr/bin/python3
for first_number in range(0, 10, 1):
    for last_number in range(first_number + 1, 10, 1):
        if first_number == 8 and last_number == 9:
             print('{}{}'.format(first_number, last_number))
        else:
             print('{}{}, '.format(first_number, last_number), end="")

