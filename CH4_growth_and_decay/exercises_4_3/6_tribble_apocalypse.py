

def tribble_apocalypse(init_pop):
    hours = 0
    tribbles = init_pop
    while tribbles < 1e6:
        tribbles = tribbles * 1.5
        hours += 1
    return hours

def soln_man():
    tribbles = 10
    hours = 0
    while tribbles < 1e6:
        tribbles = tribbles + tribbles // 2
        hours = hours + 1
    return hours

print(tribble_apocalypse(10))
print(soln_man())
