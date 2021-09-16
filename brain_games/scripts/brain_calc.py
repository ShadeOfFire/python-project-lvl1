#!/usr/bin/env python3


import prompt
import random
from brain_games import cli


def good():
    text = "Congratulations, " + cli.name + "!"
    print(text)


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
        first_n = random.randrange(2, 100, 1)
        second_n = random.randrange(2, 100, 1)
        operations_list = ['+', '-', '*']
        oper = random.choice(operations_list)
        text = 'Question: ' + str(first_n) + ' ' + oper + ' ' + str(second_n)
        print(text)
        ans = prompt.string('Your answer: ')
        correct_answer = str(result(first_n, second_n, oper))
        if ans == correct_answer:
            success = success + 1
            print("Correct!")
        else:
            wrong_text = "' is wrong answer ;(. Correct answer was '"
            text = "'" + str(ans) + wrong_text + correct_answer + "'"
            text = "Let's try again, " + cli.name + "!"
            print(text)
            break
        if success == 3:
            good()


if __name__ == '__main__':
    main()
