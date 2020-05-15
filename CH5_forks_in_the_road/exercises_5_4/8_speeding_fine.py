# Book was slightly cleaner

def fine(speed_limit, clocked_speed):

    if clocked_speed <= speed_limit:
        return 0

    base_fine = 50 + 5 * (clocked_speed - speed_limit)

    if clocked_speed < 90:
        return base_fine
    if clocked_speed > 90:
        return base_fine + 200

def sol_man(speed_limit, clocked_speed):
    if clocked_speed <= speed_limit:
        return 0
    amount = 50 + 5 * (clocked_speed - speed_limit)
    if clocked_speed > 90:
        amount += 200
    return amount

for i in [55, 40, 10, 100, 35]:
    print(fine(35, i))

for i in [55, 40, 10, 100, 35]:
    print(sol_man(35, i))


