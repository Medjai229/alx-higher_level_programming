#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c = ord(c)
        if c >= 97 and c <= 122:
            c = c - 32
        c = chr(c)
        print("{:s}".format(c), end='')
    print("")
