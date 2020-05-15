def median(data):
    """Returns the median number in a list of numbers data."""
    nums = data.copy()
    nums.sort()
    if len(nums) % 2 == 0: # if even number of elements in the list
        # median is sum of middle 2 divided by 2
        median = (nums[(len(nums) - 1) // 2] + nums[((len(nums) - 1) // 2) + 1]) / 2
    else:
        median = nums[len(nums) // 2] # max index floor 2, plus one (not adding 1 here just to subtract it again)
    return median
    

data = [2, 5, 1, 3, 4]
data_2 = [6, 3, 2, 1, 4, 5]

assert median(data) == 3, f"fail {median(data)}"
assert median(data_2) == 3.5, f"fail {median(data_2)}"
