import random

def update_ages(names, ages):
    """Takes as parameters a list, names, of people whose birthday is today and
    a dict, ages, with names as keys and ages as values, and increments the age
    of each person in the dictionary who is in names (i.e. whose birthday it is).
    """
    for key in ages:
        if key in names:
            ages[key] += 1
    # solman iterates names, not the dict. Maybe that's faster because fewer
    #   entries in names? Maybe idea is that it can be some unrelated person's
    #   birthday without that person being listed as one of the ones in ages.
    
# make dict
random.seed(6)
ages = {}
numbers = [random.randint(1, 100) for i in range(1, 6)]
people = ['Lodder', 'Hlort', 'Plogg', 'Yubboh', 'Lumpet']
names = [people[i] for i in range(0, len(people) - 1, 2)] # whose birthdays are it
i = 0
for person in people:
    ages[person] = numbers[i]
    i += 1
print(f"initial ages: {ages}")
print(f"whose birthdays are it??? : {names}")
print('---')
update_ages(names, ages)
print(f"updated ages: {ages}")
