"""https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv"""

"""Rewrite to store id and data in a single list-of-lists table."""

import urllib.request as web
import selection_sort as ss
import search_functions as sf

def get_lists():
    """Earthquake IDs and 'satellite data' from data file at
    https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv
    and returns a list containing one list per table row.

    Returns:
        quakes (list): list of lists in form [id, latitude, longitude, depth, magnitude]
    """

    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv'
    quake_file = web.urlopen(url)
    quake_file.readline() # read past header row

    quakes = []
    for line in quake_file:
        row_list = []
        line = line.decode('utf-8')
        row = line.split(',') # row as a list of its columns' values
        row_list.append(row[11])
        row_list.append(float(row[1])) # lat
        row_list.append(float(row[2])) # long
        row_list.append(float(row[3])) # depth
        row_list.append(float(row[4])) # mag
        quakes.append(row_list)
    quake_file.close()
    return quakes

def print_quakes_list(quakes):
    print(f"List would go here")
    id_width = 20
    location_width = 25
    magnitude_width = 10
    depth_width = 10
    print(
        f"{'ID':^{id_width}} {'Location':^{location_width}} \
{'Magnitude':^{magnitude_width}} {'Depth':^{depth_width}}"
        )
    print('-' * id_width + ' ' + '-' * location_width +
          ' ' + '-' * magnitude_width + ' ' + '-' * depth_width)
    for i in range(len(quakes) - 1):
        location_tuple_string = f"({quakes[i][1]}, {quakes[i][2]})"
        print(f"{quakes[i][0]:^{id_width}}" +
              f"{location_tuple_string:^{location_width}}" +
              f"{quakes[i][3]:^{magnitude_width}}" +
              f"{quakes[i][2]:^{depth_width}}")
        
def query_quakes(quakes):
    prompt = 'Earthquake ID (q to quit): '
    key = input(prompt)
    while key.lower() != 'q':
        if key.lower() == 'list':
            print_quakes_list(quakes)
        else:
            index = sf.binary_search([quakes[i][0] for i in range(len(quakes) - 1)], key, 0, len(quakes) - 1)
    ##        index = sf.linear_search(ids, key) # for comparison. Will exceed default cpython max recursion depth for worst case i.e. not-found.
            if index >=0:
                print('Location: ' + str(quakes[index][1:3]) + '\n' +
                      'Magnitude: ' + str(quakes[index][3]) + '\n' +
                      'Depth : ' + str(quakes[index][2]) + '\n')
            else:
                print('An earthquake with that ID was not found.')
        key = input(prompt)



def main():
    quakes = get_lists()
##    print(quakes)
##    assert type(data[0][0]) == float, f"type was {type(data[0][0])}"
    ids = [quakes[i][0] for i in range(len(quakes) - 1)]
    ss.selection_sort_parallel_lists(ids, quakes)
    query_quakes(quakes)

if __name__ == '__main__':
    main()
