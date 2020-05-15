import random
import time
import sys

# red tape to import the rd funcs from the parent folder
sys.path.append("C:\\Users\\Ben\\Desktop\\Python_DCS_book\\CH8_data_analysis")
from c4_remove_duplicates import remove_duplicates_1, \
     remove_duplicates_2, remove_duplicates_3
    
def create_data(n):
    """Creates a list of n random integers between 0 and n-1 using a list
    accumulator and the random.randrange function."""
    data = []
    for i in range(n):
        data.append(random.randrange(n))
    return data

def speedtest():
    """Call each of the three remove_duplicates functions."""
    n_vals = [10 ** i for i in range(2, 6)]
    functions = [remove_duplicates_1, remove_duplicates_2, remove_duplicates_3]

    test_data = {}
    for n in n_vals:
        data = create_data(n)
        test_data[n] = data

    print(f"{'':10}|{'rd1':^10}|{'rd2':^10}|{'rd3':^10}|") # :^10 means 10char min column width, aligned center (^)
    for key in test_data:
        print(f"{key:10}|{time_rd_func(functions[0], test_data[key]):10.5f}|\
{time_rd_func(functions[1], test_data[key]):10.5f}|\
{time_rd_func(functions[2], test_data[key]):10.5f}|")
        

def time_rd_func(function, data):
    """Returns the time needed to run function on data.
    Returns:
        (float): Time in seconds
    """
    start = time.time()
    uniques = function(data)
    end = time.time()
    return (end - start)

def main():
    data = create_data(10)
    assert len(data) == 10, f"fail len(data)"
    speedtest()
    rd3 = time_rd_func(remove_duplicates_3, data)


if __name__ == "__main__":
    main()
    
