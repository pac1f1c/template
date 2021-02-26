#!/usr/bin/env python

import random
import sys
import logging

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def main():
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        guess = input("Guess a number between 1 and 10: ")
        try:
            guess = int(guess)
        except ValueError:
            print("{} is not a number!".format(guess))
        else:
            if guess == secret_num:
                print("You win! My number was {}".format(guess))
                break
            elif guess < secret_num:
                logging.info("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            guesses.append(guess)

    else:
        print("You ran out of choices. My number was {}".format(secret_num))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        LOGGER.info("\nSIGINT or CTRL-C detected. Exiting")
        sys.exit(130)
