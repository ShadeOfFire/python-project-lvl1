#!/usr/bin/env python3


from brain_games import brain_logic
from brain_games import cli


def main():
    text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    cli.welcome_user(text)
    brain_logic.prime_game()


if __name__ == '__main__':
    main()
