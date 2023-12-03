#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    x = len(my_list)
    if idx >= x:
        return None
    else:
        return my_list[idx]
