import random

def monty_hall(choice, switch=False):
    """Returns true if the final-choice door was the winning door, else false.

    Args:
        choice (int): Door number matching one of the three doors 0, 1, or 2.
        switch (bool): True to simulate the player switching doors. 
    """


    doors = [0, 1, 2]
    
    doors.remove(choice)

    # Eliminate one of the remaining non-winning doors

    if choice == 0:
        doors.remove(1)
    elif choice == 1:
        doors.remove(0)
    

    if switch == True:
        choice = random.choice(doors)

    # Translate choice to a win or lose outcome--simulate opening the door
        # Car is always behind door 2 in this simulation
    if choice == 2:
        return True
    else:
        return False

def monte_carlo_monty(trials, switch):
    """
    Args:
        trials (int): Number of playthroughs of Monty Hall game to simulate.

    """
    wins = 0
    for i in range(trials):
        door = random.choice([0, 1, 2])
        result = monty_hall(door, switch)
        if result == True:
            wins += 1
    return wins / trials

def sol_man_monty_hall(choice, switch):
    car = 2
    if choice == car:
        if switch:
            win = False
        else:
            win = True
    else:
        if switch:
            win = True
            # If you didn't choose the car, you always win by switching.
        else:
            win = False
    return win

def sol_man_monte_monty(trials):
    wins = 0
    for trial in range(trials):
        choice = int(random.random() * 3)
        if sol_man_monty_hall(choice, True):
            wins = wins + 1
    return wins / trials

def main():

    trials = 10000

    win_rate = monte_carlo_monty(trials, True)
    print(f"win rate of {win_rate} for {trials} trials when switching doors")

    win_rate = monte_carlo_monty(trials, False)
    print(f"win rate of {win_rate} for {trials} trials when not switching")

    win_rate = sol_man_monte_monty(trials)
    print(f"Win rate of {win_rate} when always switching using book's function")


main()

    
