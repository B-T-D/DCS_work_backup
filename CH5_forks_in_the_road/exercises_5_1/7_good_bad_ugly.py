# [Not supposed to use dicts or tuples yet at this point in the book]

# [Mine does not work, refer to book's only]

import random

def sol_man_good_bad_ugly():
    good = good1 = 1
    bad = bad1 = 1
    ugly = ugly1 = 1
    rounds = 0
    while good + bad + ugly > 1: # While there's at least one of them left
        rounds = rounds + 1
        if good == 1: # If good is still left
            if random.random() < 0.8: # If the shot is a hit
                if bad == 1: # And if bad is still standing
                    bad1 = 0
                else:
                    ugly1 = 0 # If Bad was already dead, Good's shot hits Ugly
        if bad == 1: # If bad is still left, his shot is simulated with...
            if random.random() < 0.7: # if Bad's shot hits
                if good == 1: # if good is still standing, Bad shoots at good (either it's still a 3 way, or else it's 1v1 Bad v Good)
                    good1 = 0
                else:
                    ugly1 = 0
        if ugly == 1: # if Ugly is still in, his shot is simulated...
            if random.random() < 0.6:
                if bad == 1:
                    bad1 = 0
                else:
                    good1 = 0
        # Update each gunman at end of round, to allow for possibility for overlapping kills
        good = good1
        bad = bad1
        ugly = ugly1
    # Tally the winner at the end of the round, i.e. once there's 1 or fewer gunmen remaining such that the while loop breaks
    if good == 1:
        return 1, rounds
    if bad == 1:
        return 2, rounds
    if ugly == 1:
        return 3, rounds
    return 0, rounds # Book doesn't care about having multiple return statements 

def sol_man_monte_gbu(trials):
    total_good = 0
    total_bad = 0
    total_ugly = 0
    total_none = 0
    total_rounds = 0
    print(f"----------")
    print(f"For {trials} trials:")
    for trial in range(trials):
        winner, rounds = sol_man_good_bad_ugly()
        if winner == 1:
            total_good = total_good + 1
        elif winner == 2:
            total_bad = total_bad + 1
        elif winner == 3:
            total_ugly += 1
        else:
            total_none += 1
        total_rounds = total_rounds + rounds
    print(f"Probability that everyone dies: {total_none / trials}")
    print(f"Probability that The Good survives: { total_good / trials}")
    print(f"Probability that the Bad survives: {total_bad / trials} ")
    print(f"Probability that The Ugly survives: {total_ugly / trials}")

def shoot(hit_chance):
    """

    Args:
        hit_chance (float): Probability of the shot hitting, from 0 to 1

    Returns:
        True if the shot hit, False if missed
    """

    r = random.random()
    return True if r < hit_chance else False


def good_bad_ugly():
    """Returns 1, 2, 3, or 0 depending upon whether Good, Bad, Ugly, or nobody
    won the gunfight."""
    gunmen = ['Good', 'Bad', 'Ugly']
    while len(gunmen) > 1:
        if len(gunmen) == 3:
            shot = []
            if shoot(0.8) == True:
                shot.append('Bad') # Bad is shot if Good hits him
            if shoot(0.7) == True:
                shot.append('Good') # Bad has 0.7 chance of hitting Good
            if shoot(0.6) == True:
                shot.append('Bad')
        elif len(gunmen) == 2:
            shot = []
            print(f"remaining gunmen are {gunmen}")
            for gunman in gunmen:
                opponent = gunmen
                opponent.remove(gunman)
                opponent = opponent[0] # This gunman's target is the only other remaining gunman
                print(f"gunman is {gunman}, opponent is {opponent}")
                if gunman == 'Good':
                    if shoot(0.8) == True:
                        shot.append(opponent)
                        print(f"{gunman} shot at {opponent} and hit")
                elif gunman == 'Bad':
                    if shoot(0.7) == True:
                        shot.append(opponent)
                elif gunman == 'Ugly':
                    if shoot(0.6) == True:
                        shot.append(opponent)
                print(f"shot in this 2 gunmen round: {shot}")
        for gunman in shot:
            if gunman in gunmen:
                gunmen.remove(gunman)

    print(f"winner was {gunmen}")
    
    try:
        winner = gunmen.pop()
        if winner == 'Good':
            answer = 1
        elif winner == 'Bad':
            answer = 2
        elif winner == 'Ugly':
            answer = 3
    except IndexError:
        answer = 0
    
    return answer

def monte_gbu(trials):

    print(f"For {trials} trials:")
    # probability they all die:
    all_dead = 0
    for i in range(trials):
        winner = good_bad_ugly()
        if winner == 0:
            all_dead += 1
    print(f"Probability they all die: {all_dead / trials}")

    # Probability the Good wins:
    good_wins = 0
    for i in range(trials):
        winner = good_bad_ugly()
        if winner == 1:
            good_wins += 1
    print(f"Probability The Good survives: {good_wins / trials}")

    print('--------')


for i in range(6):
####    monte_gbu(i)
    sol_man_monte_gbu(10 ** i)

##for i in range(20):
##    print(good_bad_ugly())
    
