
def windchill(temp, wind):
    """Gives the North American metric wind chill equivalent for given
    temperature and wind speed.

    Args:
        temp: TEmperature in degrees Celsius
        wind: Wind speed at 10m in km/h

    Returns:
        (int): Equivalent wind chill in degrees Celsius, rounded to nearest
        integer.
    """
    print(f"Initial windchill() function locals: {locals()}")
    chill = 13.12 + 0.6215*temp + (0.3965*temp - 11.37) * wind**0.16
    print(f"windchill() function locals after assigning chill variable: {locals()}")
    temp = round(chill)
    return temp

def main():
    t = -3
    w = 13
    print(f"Namespace of main() before calling windchill(): {locals()}")
    chilly = windchill(t, w)
    print(f"The wind chill is {chilly}")
    print(f"locals at the end of main(): {locals()}")
    print(f"globals at end of main(): \n{globals()}")
    for key, value in globals().items():
        print(f"\t{key} : {value}")


main()
