#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argn = len(sys.argv) - 1
    for i in range(argn):
        sum += int(sys.argv[i + 1])
    print(sum)
