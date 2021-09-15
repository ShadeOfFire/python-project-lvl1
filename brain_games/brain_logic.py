import prompt
import random
from brain_games import cli
from fractions import gcd


def result_calc(a, b, c):
    if c == '+':
        return (a + b)
    if c == '-':
        return (a - b)
    if c == '*':
        return (a * b)


def result_nod(a, b):
    return gcd(a, b)


def calculations_game():
    success = 0
    while success < 3:
        first_number = random.randrange(2, 100, 1)
        second_number = random.randrange(2, 100, 1)
        operations_list = ['+', '-', '*']
        op = random.choice(operations_list)
        print('Question: ', first_number, ' ', op, ' ', second_number)
        ans = prompt.string('Your answer: ')
        correct_answer = str(result_calc(first_number, second_number, op))
        if ans == correct_answer:
            success = success + 1
            print("Correct!")
        else:
            wrong_text = "' is wrong answer ;(. Correct answer was '"
            print("'", ans, wrong_text, correct_answer, "'")
            print("Let's try again, " + cli.name)
            break
        if success == 3:
            print("Congratulations, " + cli.name)


def nod_game():
    success = 0
    while success < 3:
        first_number = random.randrange(2, 100, 1)
        second_number = random.randrange(2, 100, 1)
        print('Question: ', first_number, ' ', second_number)
        ans = prompt.string('Your answer: ')
        correct_answer = str(result_nod(first_number, second_number))
        if ans == correct_answer:
            success = success + 1
            print("Correct!")
        else:
            wrong_text = "' is wrong answer ;(. Correct answer was '"
            print("'", ans, wrong_text, correct_answer, "'")
            print("Let's try again, " + cli.name)
            break
        if success == 3:
            print("Congratulations, " + cli.name)
