# Welcome function module


import prompt


name = None


def welcome_user(game_instructions):

    # Welcome function
    global name
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game_instructions)
