from itertools import count, cycle, combinations

nums = [0, 108, 127, 146, 342, 325, 308, 704, 721, 738, 504, 523, 542]
for c in combinations(nums, 5):
    if sum(c) == 2025:
        print(c)

def count_func():
    # Used to count infinitely
    counter = count(0, 5)

    for thing in counter:
        print(thing)
        if thing == 100:
            break

def cycles_func():
    # Allows you to infinitely cycle through a iterable sequence such as a list, tuple or a string
    i = 0
    cycler = cycle("ABCD")
    while i < 10:
        print(next(cycler), end=" ")
        i += 1

cycles_func()