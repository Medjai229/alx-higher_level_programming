#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1

if number < 0:
    sign = -1
    number = number * -1

last = number % 10

if sign == -1:
    number = number * sign
    last = last * sign

if last > 5:
    print("Last digit of {:d} is {:d} \
and is greater than 5".format(number, last))
elif last == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))
else:
    print("Last digit of {:d} is {:d} \
and is less than 6 and not 0".format(number, last))
