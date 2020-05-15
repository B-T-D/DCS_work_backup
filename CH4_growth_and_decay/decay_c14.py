import matplotlib.pyplot as pyplot
import time

def decay_c14(original_amount, years, dt):
    """Approximates the continuous decay of carbon-14.

    Args:
        original_amount (float): The original quantiy of carbon-14 (grams)
        years (int): Number of years to simulate
        dt (float): Value of "delta t" in the simulation (fraction of a year)

    Returns:
        (float): Final quantity of carbon-14 (grams)
    """

    start_time = time.time()
    k = -0.000121
    amount = original_amount
    t = 0
    time_list = [0] # x values for plot
    amount_list = [amount] # y values for plot

    lists_computation_start = time.time()
    for step in range(1, int(years/dt) + 1):
        amount = amount + k * amount * dt
        t = step * dt
        time_list.append(t)
        amount_list.append(amount)
    lists_computation_end = time.time()
    lists_computation_speed = lists_computation_end - lists_computation_start

    print(
        f"dt of {dt}: Computations of the time_list and amount_list took {lists_computation_speed} seconds")

##    pyplot.plot(time_list, amount_list)
    pyplot.xlabel('Years')
    pyplot.ylabel('Quantity of carbon-14')
    pyplot.show()
##    end_time = time.time()

##    execution_time = end_time - start_time
##    print(f"decay_c14() function ran in {execution_time}")

    return amount

for i in [1, 0.5, 0.1, 0.01, 0.001]:
    decay_c14(original_amount=100, years=5000, dt=i)
