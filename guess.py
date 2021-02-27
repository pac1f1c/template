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
            logging.info("%s is not a number!", guess)
        else:
            if guess == secret_num:
                logging.info("You win! My number was %s", guess)
                break
            elif guess < secret_num:
                logging.info("My number is higher than %s", guess)
            else:
                logging.info("My number is lower than %s", guess)
            guesses.append(guess)
    else:
        logging.info("You ran out of choices. My number was %s", secret_num)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        LOGGER.info("\nSIGINT or CTRL-C detected. Exiting")
        sys.exit(130)
