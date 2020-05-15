import random, math

def perfect_square(number):
    """Original function for reference."""
    if number < 0:
        return False
    else:
        return math.sqrt(number) == int(math.sqrt(number))

def perfect_square_refactor(number):
    return math.sqrt(number) == (int(math.sqrt(number))) and not(number < 0)
        # not() was hacky for big picture time prioritization
            # Book had no qualms just changing to number >= 0, which was my
                #   first instinct before using not().

def sol_man(number):
    return (number >= 0) and (math.sqrt(number) == int(math.sqrt(number)))


list = [i**2 for i in range(13)]

for i in range(13):
    list.append(i ** 2 + random.random())


for e in list:
    print(f"number = {e}")
    print(f"{e}  | {perfect_square(e)}  | {perfect_square_refactor(e)} | {sol_man(e)}")
    
