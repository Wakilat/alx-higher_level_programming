#!/usr/bin/python3
def common_elements(set_1, set_2):
    for i in set_1:
        for i in set_2:
            if set_1[i] == set_2[i]:
                return i
