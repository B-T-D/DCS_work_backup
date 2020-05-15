#!/usr/bin/env python3

import random

def guessingGame(maxGuesses):
    """ (docstring omitted) """
    
    secretNumber = random.randrange(1, 101)
    myGuess = 0
    guesses = 0
    while (myGuess != secretNumber) and (guesses < maxGuesses):
        myGuess = input('Please guess my number: ')
        myGuess = int(myGuess)
        guesses = guesses + 1         # increment # of guesses used
        
        if (myGuess != secretNumber) and (guesses < maxGuesses):
            if myGuess < secretNumber:          # guess is too low
                print('Too low.  Try again.')   #   give a hint
            else:                               # guess is too high
                print('Too high.  Try again.')  #   give a hint
                
    if myGuess == secretNumber:        # win
        print('You got it!')
    else:                              # lose
        print('Too bad.  You lose.')

def main():
    guessingGame(10)

main()
