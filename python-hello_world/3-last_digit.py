#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
    answer = number % 10
    if answer > 5:
        print("Last digit of {} is {} and is greater than 5".format(number,answer))
    elif answer == 0:
        print("Last digit of {} is {} and is 0".format(number,answer))
    elif answer < 6 and answer != 0:
        print("Last digit of {} is {} and is less than 6 and not 0".format(number,answer))

else:
    answer = (-number) % 10
    print("Last digit of {} is -{} and is less than 6 and not 0".format(number,answer))
