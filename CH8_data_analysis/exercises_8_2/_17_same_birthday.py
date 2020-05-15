import random

def same_birthday(people):
    """Creates a list of people random birthdays and returns True if
    two birthdays are the same, else False.

    Uses 0 throuth 364 to represent 365 possible unique birthdays in a year. 
    """
    birthdays = []
    for i in range(people):
        birthdays.append(random.randint(0, 364))
    # check if any two are same:
    for b in birthdays:
        if birthdays.count(b) > 1:
            return True
    return False

def birthday_problem(people, trials):
    """Returns the probability that, in a room with the given number of people,
    for trials simulations, two share the same birthday."""
    same_birthdays_count = 0
    for i in range(trials):
        if same_birthday(people):
            same_birthdays_count += 1
    return same_birthdays_count / trials
    

def birthday_problem_2(trials):
    """Return the smallest number of people for which the probability of a pair sharing a birthday is
    at least 0.5."""
    probability = 0
    people = 1
    while probability < 0.5:
        people += 1
        probability = birthday_problem(people, trials)
    return people


trials_counts = [1, 10, 100, 1000, 5000, 10000]
for trials in trials_counts:
    print(f"{birthday_problem_2(trials)} is smallest group that has at least 0.5 probability of overlap, with {trials} trials")    
    
print(same_birthday(100000))
print(birthday_problem(10, 10000))

tests = [10 ** i for i in range(7)]
tests = [5, 6, 7, 8, 9, 10, 15, 20]
print(tests)
trials = 1000
for t in tests:
    probability = round((birthday_problem(t, trials)), 6)
    print(probability)
##    print(f"with {t} people, {probability} probability of same birthday after {trials} trials")
                         
    
