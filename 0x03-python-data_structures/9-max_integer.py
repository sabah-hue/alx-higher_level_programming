#!/usr/bin/python3
def max_integer(my_list=[]):
    check = len(my_list)
    if check == 0:
        return None
    else:
        max = my_list[0]
        for i in range(check):
            if my_list[i] > max:
                max = my_list[i]
        return max
