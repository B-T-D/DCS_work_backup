
def monitor(temperature):

    return temperature >= 97.9 and temperature <= 99.3

test_temps = [0, 98.6, 97.6, 101.0, 99.3, 97.9]
for temp in test_temps:
    print(monitor(temp))
