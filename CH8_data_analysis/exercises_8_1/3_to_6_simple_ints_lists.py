

def sum_list(data):
    sum = 0
    for e in data:
        sum += e
    return sum


def sum_odds(data):
    sum = 0
    for e in data:
        if e % 2 != 0:
            sum += e
    return sum

def count_odds(data):
    sum = 0
    for e in data:
        if e % 2 != 0:
            sum += 1
    return sum

def multiples5(data):
    count = 0
    for e in data:
        if e % 5 == 0:
            count += 1
    return count

test = [5, 4, 3, 2, 1]
print(sum(test))

test = [1, 2, 3]
assert sum_odds(test) == 4, f"sum_odds() fail, sum_odds([1,2,3]) returned \
{sum_odds(test)}"

assert count_odds(test) == 2, f"count_odds() fail, returned {count_odds(test)}"

test = [5, 7, 2, 10]
assert multiples5(test) == 2, f"multiples5() fail, returned {multiples5(test)}"
