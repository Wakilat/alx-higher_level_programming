#!/usr/bin/python3
def print_arg(argv):
    n = len(arg) - 1
    if n == 0:
        print("{} argument.".format(n))
        return
    else:
        if n == 1:
            print("{} arguments:".format(n))
        else:
            print("{} arguments:".format(n))
        i = 1
        while i <= n:
            print("{}: {}".format(n, argv[i]))
            i += 1


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
