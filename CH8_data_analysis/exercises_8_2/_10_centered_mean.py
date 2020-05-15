def centered_mean(data):
    nums = data.copy() # copy it to not mutate the original
    nums.sort()
    nums.pop(0) # first value will be lowest
    nums.pop(-1) # last value will be highest
    return sum(nums) / len(nums)

# solman uses data.remove(min(data)), then same for max. It doesn't care
#   about modifying original list. 


data = [2, 10, 3, 5]

assert centered_mean(data) == 4, f"fail {centered_mean(data)}"
