# Welcome function module


import prompt


name = None


def welcome_user():

    # Welcome function
    global name
    name = prompt.string('May I have your name?')
    print('Hello, ' + name + '!')
