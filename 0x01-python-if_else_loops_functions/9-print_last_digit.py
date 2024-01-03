#!/usr/bin/python3
def print_last_digit(number):
    if number < -1:
        number = number * -1

    last = number % 10
    print("{:d}".format(last), end='')
    return last
