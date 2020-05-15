
def bonus(salaries):
    """Increases every value in the dict by 5%"""
    for key in salaries:
        salaries[key] += 0.05 * salaries[key]




salaries = {}
numbers = [i * 20 for i in range(1, 6)]
people = ['Lodder', 'Hlort', 'Plogg', 'Yubboh', 'Lumpet']
i = 0
for person in people:
    salaries[person] = numbers[i]
    i += 1

    
print(salaries)
print('---')
bonus(salaries)
print(salaries)
