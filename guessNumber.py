import random

# user is guessing the random number which computer has created
def guess(x):
    random_num = random.randint(1, x)
    guess_num = 0
    while guess_num != random_num:
        guess_num = int(input(f"Guess a number between 1 and {x}: "))
        if guess_num < random_num:
            print("number is too low")
        elif guess_num > random_num:
            print("number is too high")
        else:
            print(f"random number is: {guess_num}")


# computer is guessing the random number which the user has created
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C).lower(): ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print(f"Yay! Computer guessed the number correctly {guess}")







# guess(30)
computer_guess(30)
