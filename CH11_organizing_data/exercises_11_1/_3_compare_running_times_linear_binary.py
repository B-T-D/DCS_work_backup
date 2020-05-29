from matplotlib import pyplot
import time
import sys

import search_functions as sf


def get_running_time_binary(keys):
    """Returns the running time for the binary search function.
    Uses target of -1. 

    Args:
        keys (list): list of positive, consecutive integers (i.e. not
            containing -1)

    Returns:
        (float): time in seconds required for the function to execute
            once on the list keys.
    """
    target = -1
    start = time.time()
    sf.binary_search(keys, target, 0, len(keys) - 1)
    end = time.time()
    return end - start
    
def get_running_time_linear(keys):
    """Returns the running time for the linear search function. Uses
    target of -1.

    Args:
        keys (list): list of positive, consecutive integers (i.e. not
            containing -1)

    Returns:
        (float): time in seconds required for the function to execute once
            on the list keys.
    """
    target = -1
    start = time.time()
    sf.linear_search(keys, target)
    end = time.time()
    return end - start

def plot_times(min_length, max_length, step):
    """Produces a plot comparing the worst case running times for binary search
    and linear search on lists with length between min_length and max_length.

    Returns:
        None
    """

    # As the book does it, function is forced to round to zero, because the
    #   float returned by time.time() only has 6 or so decimal places.
    # Calling each more than once produces a better looking graph.

    # Binary search is so fast that the book's suggested method of speed-testing
    #   doesn't even work on a reasonably fast desktop...
    max_list = list(range(max_length))
    len_keys = []
    seconds_linear = []
    seconds_binary = []
    for i in range(min_length, max_length + 1, step):
        keys = max_list[:i]
        start = time.time()
        for i in range(10):
            sf.linear_search(keys, -1)
        end = time.time()
        seconds_linear.append(end - start)
##        print(f"Linear:\n\tstart was {start}\n\tend was {end}")

        start = time.time()
        for i in range(10):
            sf.binary_search(keys, -1, 0, len(keys))
        end = time.time()
        seconds_binary.append(end - start)


    # pyplot calls

    pyplot.plot(range(min_length, max_length + 1, step), seconds_linear,
                label='Linear search')
    pyplot.plot(range(min_length, max_length + 1, step), seconds_binary,
                label='Binary search')
    pyplot.legend(loc='upper center')
    pyplot.xlabel('len(keys)')
    pyplot.ylabel('Time in seconds')
    pyplot.show()
    
##    pyplot.plot(len_keys, seconds_linear)
##    pyplot.plot(len_keys, seconds_binary)
##    pyplot.xlabel('len(keys)')
##    pyplot.ylabel('Time in seconds')
##    pyplot.show()
##    pyplot.scatter(len_keys, seconds_linear)
##    pyplot.show()
        
    

def main():
    min_length = 1
    max_length = 2500
    current_recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(max(current_recursion_limit, max_length))
    step = 50
    plot_times(min_length, max_length, step)

##sys.setrecursionlimit(3000)
##seconds_linear = []
##len_keys = []
##step = 1
##max_length = 2500
##step = 10
##min_length = -1
##
##for i in range(max_length, min_length, -step):
##    keys = list(range(i))
####    print(len(keys))
##    
##    linear_time = get_running_time_linear(keys)
##    if linear_time > 0:
##        len_keys.append(len(keys))
##        seconds_linear.append(linear_time)
##
##
##pyplot.plot(len_keys, seconds_linear)



##sys.setrecursionlimit(2000)
##max_length = 
##keys = make_list(max_length)
##target = -1
##start = time.time()
##sf.binary_search(keys, target, 0, len(keys) - 1)
##end = time.time()
##running_time = round(end - start, ndigits=100)
##linear_run = get_running_time_linear(keys)
##print(linear_run)

if __name__ == '__main__':
    main()
