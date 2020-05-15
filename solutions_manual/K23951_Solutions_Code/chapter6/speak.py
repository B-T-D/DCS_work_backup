#!/usr/bin/env python3

def roar(n):
    return 'r' + ('o' * n) + ('a' * n) + 'r!'

def speak(animal):
    if animal == 'cat':
        word = 'meow.'
    elif animal == 'dog':
        word = 'roof.'
    else:
        word = roar(10)
      
    print('The', animal, 'says', word)
   
speak('monkey')
