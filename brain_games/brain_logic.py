import prompt
import random
import math
from brain_games import cli


def good():
    text = "Congratulations, " + cli.name + "!"
    print(text)


def result_nod(a, b):
    return math.gcd(a, b)


def result_progression(start, step, index):
    return (start + step * index)


def result_prime(num):
    for i in range(2, math.floor(math.sqrt(num))):
        if (num % i) == 0:
            return ('no')
    return ('yes')


def nod_game():
    success = 0
    while success < 3:
        first_number = random.randrange(2, 100, 1)
        second_number = random.randrange(2, 100, 1)
        text = 'Question: ' + str(first_number) + ' ' + str(second_number)
        print(text)
        ans = prompt.string('Your answer: ')
        correct_answer = str(result_nod(first_number, second_number))
        if ans == correct_answer:
            success = success + 1
            print("Correct!")
        else:
            wrong_text = "' is wrong answer ;(. Correct answer was '"
            text = "'" + ans + wrong_text + correct_answer + "'"
            text = "Let's try again, " + cli.name + "!"
            print(text)
            break
        if success == 3:
            good()


def progression_game():
    success = 0
    while success < 3:
        first_number = random.randrange(2, 10, 1)
        prog_step = random.randrange(1, 5, 1)
        mis_num = random.randrange(1, 10, 1)
        text = 'Question: ' + str(first_number) + ' '
        print(text, end='')
        for i in range(10):
            if (i + 1) == mis_num:
                print('.. ', end='')
            else:
                print(first_number + prog_step * (i + 1), end='')
        print()
        ans = prompt.string('Your answer: ')
        correct_ans = str(result_progression(first_number, prog_step, mis_num))
        if ans == correct_ans:
            success = success + 1
            print("Correct!")
        else:
            wrong_text = "' is wrong answer ;(. Correct answer was '"
            text = "'" + ans + wrong_text + correct_ans + "'"
            text = "Let's try again, " + cli.name + "!"
            print(text)
            break
        if success == 3:
            good()


def prime_game():
    success = 0
    while success < 3:
        number = random.randrange(2, 100, 1)
        print('Question:', number)
        ans = prompt.string('Your answer: ')
        correct_answer = result_prime(number)
        if ans == correct_answer:
            success = success + 1
            print("Correct!")
        else:
            wrong_text = "' is wrong answer ;(. Correct answer was '"
            text = "'" + ans + wrong_text + str(correct_answer) + "'"
            print(text)
            text = "Let's try again, " + cli.name + "!"
            print(text)
            break
        if success == 3:
            good()
