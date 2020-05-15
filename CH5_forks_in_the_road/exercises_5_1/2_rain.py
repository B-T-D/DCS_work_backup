import random

def weather():
    r = random.random()
    if r < 0.7:
        print("gon rain")
    else:
        print("am not to raining")

def weather_snow():
    r = random.random()
    if r < 0.66:
        print("Snow")
    elif r < 0.99:
        print("Sun")
    else:
        print("Rain cats and dogs")


for i in range(20):
    weather()

for i in range(2000):
    weather_snow()
