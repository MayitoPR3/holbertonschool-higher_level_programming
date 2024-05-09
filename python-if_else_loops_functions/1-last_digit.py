#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lsdigit = number % -10
else:
    lsdigit = number % 10

if  lsdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lsdigit))
elif lsdigit < 6 and lsdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lsdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))