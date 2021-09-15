#!/usr/bin/env python3


from brain_games import brain_logic
from brain_games import cli


def main():
    cli.welcome_user('Find the greatest common divisor of given numbers.')
    brain_logic.nod_game()


if __name__ == '__main__':
    main()
