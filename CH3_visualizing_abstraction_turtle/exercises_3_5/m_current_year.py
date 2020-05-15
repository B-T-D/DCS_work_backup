"""
Ex 3.5.13
2020-03-28 21:23
"""

import time

def year():
    seconds = time.time() # Start with seconds since 1/1/1970
    years = seconds / 60 / 60 / 24 / 365.25 # Convert to years
    return int(years + 1970) # Convert to years since 0 CE

print(year())
