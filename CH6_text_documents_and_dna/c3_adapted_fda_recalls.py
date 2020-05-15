"""
Adapted from book's, to work with the somewhat different xml I was able to
find as of 2020-04-23.
"""

import urllib.request as web

def print_products():
    """Print the products on the FDA recall list.

    Args:
        none

    Returns:
        None
    """

    url = 'https://www.fda.gov/media/124800/download' # Similar working one as of Apr. 2020
    webpage = web.urlopen(url)

    line = ''
    # Read past headers:
    while line[:12] != '<Recallsdata':
        line = webpage.readline()
        line = line.decode('utf-8')

    product_num = 1
    # Read the first '<recall>' line (analogous to book '<PRODUCT>' line):
    line = webpage.readline()
    line = line.decode('utf-8')
    while not ('</Recallsdata>' in line): # while not more recalls
        print(product_num)
        while not '</recall>' in line: # print one recall element
            print(line.rstrip())
            line = webpage.readline()
            line = line.decode('utf-8')
        print(line.rstrip())
        product_num = product_num + 1
        line = webpage.readline() # Read next <recall> line
        line = line.decode('utf-8')
    webpage.close()

print_products()
