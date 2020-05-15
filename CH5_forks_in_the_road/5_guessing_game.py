import random

def guessing_game(max_guesses):
    """Plays a guessing game. Human player tries to guess computer's number
    from 1 to 100.

    Args:
        max_guesses (int): Maximum number of guesses allowed.

    Returns:
        None
    """

    secret_number = random.randrange(1, 101) # Integer in [1..100]

    guess = None
    guesses = 0
    while(guess != secret_number) and (guesses < max_guesses):
        guess = input(f'Please guess the number ({guesses} prior guesses): ')
        guess = int(guess)
        guesses = guesses + 1
        if (guess != secret_number) and (guesses < max_guesses):
            if guess < secret_number:
                print(f'Too low. Try again ({max_guesses - guesses} guesses left).')
            else:
                print(f'Too high. Try again ({max_guesses - guesses} guesses left).')

    if guess == secret_number: # win
        print('You got it!')
    else: # lose
        print('Too bad, you ran out of guesses. You lost.')

    print(f"number was {secret_number}")

guessing_game(10)
    
