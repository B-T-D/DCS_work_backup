import random

def loaded():
    r = random.random()
    if r < 0.25:
        roll = 1
    elif r < 0.5:
        roll = 6
    else:
        roll = random.choice([2, 3, 4, 5])
    print(roll)
    return roll


for i in range(100):
    loaded()
