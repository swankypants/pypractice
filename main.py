import random

def guess(x):

    random_number = random.randint(1, 10)
    guess = 0

    while guess != random_number:
        guess = int(input('enter a number between 1 and 10: '))
        if random_number < guess:
            print('guess too high try again')
        if random_number > guess:
            print('guess too low try again')

    print(f'you win {random_number}')

guess(10)