# Welcome function module


import prompt


def welcome_user():

    # Welcome function
    name = prompt.string('May I have your name?')
    print('Hello, ' + name + '!')
