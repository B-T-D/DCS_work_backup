#!/usr/bin/env python3

def windChill(temp, wind):
    """Gives the North American metric wind chill equivalent 
       for given temperature and wind speed.
    
    Parameters:
        temp: temperature in degrees Celsius
        wind: wind speed at 10m in km/h
        
    Return value:
        equivalent wind chill in degrees Celsius, rounded to
        the nearest integer
    """
    
    print('Local namespace at the start of windChill:', locals())
    chill = 13.12 + 0.6215 * temp + (0.3965 * temp - 11.37) * wind ** 0.16
    temp = round(chill)
    print('Local namespace at the end of windChill:', locals())
    return temp
    
def main():
    t = -3
    w = 13
    print('Local namespace in main before calling windChill:', locals())
    chilly = windChill(t, w)
    print('The wind chill is', chilly)
    print('Local namespace in main after calling windChill:', locals())
    print('Global namespace:', globals())
    
main()