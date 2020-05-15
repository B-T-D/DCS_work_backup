# Book does a long chain of ifs 

def zodiac(year):
    """Takes a four digit year and returns its Chinese zodiac animal as a
    string."""

    animals = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox',
               'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat']

    index = year % 12
    animal = animals[index]
    return animal

for i in range(2004, 2016):
    print(f"i is {i}")
    print(zodiac(i))
