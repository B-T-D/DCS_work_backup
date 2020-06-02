"""https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv"""

"""Completion of the chapter + exercises program to query the quake data."""

import urllib.request as web
import selection_sort as ss
import search_functions as sf

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
        data.append(
            (float(row[1]), float(row[2]), float(row[3]), float(row[4]))
            ) # lat, long, depth, mag
    quake_file.close()
    return ids, data

def query_quakes(ids, data):
    prompt = 'Earthquake ID (q to quit): '
    key = input(prompt)
    while key.lower() != 'q':
        index = sf.binary_search(ids, key, 0, len(ids) - 1)
##        index = sf.linear_search(ids, key) # for comparison. Will exceed default cpython max recursion depth for worst case i.e. not-found.
        if index >=0:
            print('Location: ' + str(data[index][:2]) + '\n' +
                  'Magnitude: ' + str(data[index][3]) + '\n' +
                  'Depth : ' + str(data[index][2]) + '\n')
        else:
            print('An earthquake with that ID was not found.')
        key = input(prompt)



def main():
    ids, data = get_lists()
    print(data[0][0])
    assert type(data[0][0]) == float, f"type was {type(data[0][0])}"
    ss.selection_sort_parallel_lists(ids, data)
    query_quakes(ids, data)

if __name__ == '__main__':
    main()
