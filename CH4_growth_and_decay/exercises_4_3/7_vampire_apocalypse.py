def vampire_apocalypse(v, k, vampires, people):
    """
Args:
    v (int) : The number of people each vampire converts into a vampire per day.
    k (int) : Number of vampires killed by vampire hunters each day. 
"""
    town_pop = people
    vampires = vampires
    days = 0
    while town_pop > 0:
        town_pop -= (v * vampires)
        vampires = vampires + vampires * v - k
        days += 1
    return days

def soln_man(v, k, vampires, people):
    days = 0
    while people > 0:
        people = people - vampires * v
        vampires = vampires + vampires * v - k
        days = days + 1
    return days
        


v = 2
k = 1
vampires = 5
people = 1000

print(vampire_apocalypse(v, k, vampires, people))
print(soln_man(v, k, vampires, people))
