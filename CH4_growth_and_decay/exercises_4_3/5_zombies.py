def zombie_apocalypse():
    zombies = 1
    days = 0
    world_pop = 7e9
    while zombies < world_pop:
        zombies += 2 * zombies # each zombie converts two non-zombies daily
        days += 1

    return days

print(zombie_apocalypse())
