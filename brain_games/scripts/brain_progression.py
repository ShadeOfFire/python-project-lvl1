#!/usr/bin/env python3


from brain_games import brain_logic
from brain_games import cli


def main():
    cli.welcome_user('What number is missing in the progression?')
    brain_logic.progression_game()


if __name__ == '__main__':
    main()
