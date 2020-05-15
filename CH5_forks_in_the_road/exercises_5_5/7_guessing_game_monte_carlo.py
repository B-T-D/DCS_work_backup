import random
import matplotlib.pyplot as pyplot

def guess_random(max_number):
    """Play the guessing game by making random guesses.

    Args:
        max_number(int): Highest number that can be the answer in the game.

    Returns:
        (int): Number of guesses required to guess the number in one trial. 
    
    """
    secret_number = random.randrange(1, max_number + 1)
    guess = 0
    guesses = 0
    while (guess != secret_number):
        guess = random.randrange(1, max_number + 1)
        guesses = guesses + 1

    return guesses


def guess_incremental(max_number):
    """Guess incrementally starting from the minimum end of the range."""
    secret_number = random.randrange(1, max_number + 1)
    guess = 0
    guesses = 0
    while (guess != secret_number):
        guess = guess + 1
        guesses = guesses + 1
    return guesses

def guess_narrowing(max_number):
    secret_number = random.randrange(1, max_number + 1)
    guess = 0
    low = 1
    high = max_number
    guesses = 0
    while (guess != secret_number):
        guess = (low + high) // 2
        guesses = guesses + 1
        if guess < secret_number:
            low = guess + 1
        elif guess > secret_number:
            high = guess - 1
    return guesses

def monte_carlo_random(trials, max_number):
    guesses_random = []
    for i in range(trials):
        guesses_random.append(guess_random(max_number))
    return sum(guesses_random) / trials

def monte_carlo_incremental(trials, max_number):
    guesses = []
    for i in range(trials):
        guesses.append(guess_incremental(max_number))
    return sum(guesses) / trials

def monte_carlo_narrowing(trials, max_number):
    guesses = []
    for i in range(trials):
        guesses.append(guess_narrowing(max_number))
    return sum(guesses) / trials


def plot_guesses(trials):
    max_numbers = [i for i in range(5, 101, 5)]
    avg_random = []
    avg_incremental = []
    avg_narrowing = []
    for n in max_numbers:
        avg_random.append(monte_carlo_random(trials, n))
        avg_incremental.append(monte_carlo_incremental(trials, n))
        avg_narrowing.append(monte_carlo_narrowing(trials, n))

    pyplot.plot(max_numbers, avg_random, label='guess_random')
    pyplot.plot(max_numbers, avg_incremental, label='incremental')
    pyplot.plot(max_numbers, avg_narrowing, label='narrowing')
    pyplot.legend(loc = 'center right')
    pyplot.xlabel('max possible secret number')
    pyplot.ylabel('mean guesses required')
    pyplot.show()
        
    
plot_guesses(100000)

    
