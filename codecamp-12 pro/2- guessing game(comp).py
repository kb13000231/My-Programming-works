import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}:"))
        if guess < random_number:
            print('Sorry,guess again number is too low.')
        elif guess > random_number:
            print('Sorry,guess again number is too high.')

    print(f'Congratulations!! You have guessed the number {guess} correctly! ')


guess(int(input('Upper bound: ')))