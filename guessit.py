#!/usr/bin/env python

import random
import sys

answer = random.randint(1,20)
print("I'm guessing a number from 1 to 20.")
print("Can you guess it?")

while True:
    try:
        guess = int(input())
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
if guess > answer:
    print("The answer is too high!")
elif guess < answer:
    print("The answer is too low!")
else:
    print("Got it!")
