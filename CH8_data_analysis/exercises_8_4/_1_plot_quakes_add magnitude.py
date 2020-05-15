"""Plot earthquakes from
https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv
"""

import urllib.request as web
from matplotlib import pyplot

def plot_quakes():
    """Plot the locations of all earthquakes in the past month.

    Args:
        None

    Returns:
        None
    """

    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv'
    quake_file = web.urlopen(url)
    header = quake_file.readline() # read past the header row to get to the data

    longitudes = []
    latitudes = []
    depths = []
    magnitudes = []
    for line in quake_file:
        line = line.decode('utf-8')
        # split (str) line at every comma, since commas separate rows in CSV:
        row = line.split(',')
        # convert each row value to a float then append to its respective list:
        latitudes.append(float(row[1])) # row[0] is the datetime
        longitudes.append(float(row[2]))
        depths.append(float(row[3]))
        try:
            magnitudes.append(float(row[4]))
        except ValueError:
            print(f"Couldn't append '{row[4]}' to magnitudes as float \
earthquake {row[0]}")
    quake_file.close()

    # Create a list of colors to use in display (color points by depth)
    colors = []
    for depth in depths:
        if depth < 10:
            colors.append('yellow')
        elif depth < 50:
            colors.append('red')
        else:
            colors.append('blue')

    # Create list of sizes
    sizes = [mag ** 2 for mag in magnitudes]

    # plot the earthquakes in their respective colors and dot sizes:
    pyplot.scatter(longitudes, latitudes, s = sizes, color = colors)
    pyplot.show()

plot_quakes()
