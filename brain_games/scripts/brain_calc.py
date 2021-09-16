#!/usr/bin/env python3


import prompt
import random
from brain_games import cli


def result(a, b, c):
    if c == '+':
        return (a + b)
    if c == '-':
        return (a - b)
    if c == '*':
        return (a * b)


def main():
    cli.welcome_user('What is the result of the expression?')
    success = 0
    while success < 3:
        first_number = random.randrange(2, 100, 1)
        second_number = random.randrange(2, 100, 1)
        operations_list = ['+', '-', '*']
        operation = random.choice(operations_list)
        print('Question: ', first_number, ' ', operation, ' ', second_number)
        ans = prompt.string('Your answer: ')
        correct_answer = str(result(first_number, second_number, operation))
        if ans == correct_answer:
            success = success + 1
            print("Correct!")
        else:
            wrong_text = "' is wrong answer ;(. Correct answer was '"
            text = "'" + str(ans) + wrong_text + correct_answer + "'"
            print(text)
            print("Let's try again, " + cli.name)
            break
        if success == 3:
            print("Congratulations, " + cli.name)


if __name__ == '__main__':
    main()
