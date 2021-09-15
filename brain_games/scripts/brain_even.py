#!/usr/bin/env python3


import prompt
import random
from brain_games import cli


def result(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def main():
    rules = 'Answer "yes" if the number is even, otherwise answer "no"'
    cli.welcome_user(rules)
    success = 0
    while success < 3:
        qnumber = random.randrange(2, 100, 1)
        print('Question: ', qnumber)
        answer = prompt.string('Your answer: ')
        if answer == result(qnumber):
            success = success + 1
            print("Correct!")
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + cli.name)
            break
    if success == 3:
        print("Congratulations, " + cli.name)


if __name__ == '__main__':
    main()
