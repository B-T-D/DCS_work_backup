import random
import matplotlib.pyplot as pyplot

def roll():
    r = random.random()
    if r < 0.167:
        roll = 1
    elif r < 0.333:
        roll = 2
    elif r < 0.5:
        roll = 3
    elif r < 0.667:
        roll = 4
    elif r < 0.833:
        roll = 5
    else:
        roll = 6
    return roll

def roll_book():
    r = random.random()
    if r < 1 / 6:
        roll = 1
    elif r < 1 / 3:
        roll = 2
    elif r < 1 / 2:
        roll = 3
    elif r < 2/ 3:
        roll = 4
    elif r < 5/ 6:
        roll = 5
    else:
        roll = 6
    return roll

def draw_roll_histogram(trials):
    rolls = []
    for trial in range(trials):
        sum = roll_book() + roll_book()
##        sum = roll() + roll()
        rolls.append(sum)
    pyplot.hist(rolls, 11)
    pyplot.show()

draw_roll_histogram(10000)
##print(roll())

