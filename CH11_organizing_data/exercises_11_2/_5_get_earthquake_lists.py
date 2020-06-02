"""https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv"""

import urllib.request as web

def get_lists():
    """Earthquake IDs and 'satellite data' from data file at
    https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv
    and returns two parallel lists.

    Returns:
        ids (list): a list containing the earthquake ID values
        data (list): a list of tuples containing the satellite data. Tuples
            in form (latitude, longitude, depth, magnitude).
    """

    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv'
    quake_file = web.urlopen(url)
    quake_file.readline() # read past header row

    ids = []
    data = []
    for line in quake_file:
        line = line.decode('utf-8')
        row = line.split(',') # row as a list of its columns' values
        ids.append(row[11])
        data.append((row[1], row[2], row[3], row[4])) # lat, long, depth, mag
    return ids, data


def main():
    ids, data = get_lists()
    print(data)

if __name__ == '__main__':
    main()
