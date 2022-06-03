#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cpy_my_list = my_list.copy()
    if idx < 0:
        return cpy_my_list
    elif idx > len(my_list) - 1:
        return cpy_my_list
    else:
        return cpy_my_list[idx] = element
