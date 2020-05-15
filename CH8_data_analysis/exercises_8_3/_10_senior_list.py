import random

def senior_list(students, year):
    """Takes as a pareameter a dict named studends, with names a skeys and
    class years as valuues, and returns a list of names of students who are
    graduating in year."""
    senior_list = []
    for key in students:
        if students[key] == year:
            senior_list.append(key)
    return senior_list

# build the dict
people = ['Lodder', 'Hlort', 'Plogg', 'Yubboh', 'Lumpet', 'Flirge',
          'Rebekkaknee', 'Slutwagon', 'Cumdump', 'Twinkford']
years = [2020, 2021, 2022, 2023]
students = {}
random.seed(1)
for person in people:
    students[person] = random.choice(years)

print(students)
assert senior_list(students, 2024) == [], 'fail no one in the test dict \
graduates later than 2023'

seniors_2023 = senior_list(students, 2023)

assert 'Slutwagon' in seniors_2023, f'fail, with this seed \
Slutwagon gets 2023 {seniors_2023}'
