#!/usr/bin/python3
for i in range("a", "z" + 1):
    if i == "q" or i == "e":
        continue
    else:
        print("{:s}".format(i), end="")
