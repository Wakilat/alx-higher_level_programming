#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while True:
        try:
            if i < x:
                print(my_list[i], end='')
                index += 1
            else:
                return i
        except IndexError:
            return i
