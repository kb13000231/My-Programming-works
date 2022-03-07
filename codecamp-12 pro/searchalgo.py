import random
import time


def naive_search(ls, target):
    for i in range(len(ls)):
        if ls[i] == target:
            return i
    return -1


def binary_search(ls, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(ls) - 1

    if high < low:
        return -1

    midpoint = (low + high)//2
    if ls[midpoint] == target:
        return midpoint
    elif ls[midpoint] > target:
        return binary_search(ls, target, low, midpoint-1)
    else:
        return binary_search(ls, target, midpoint+1, high)


if __name__ == '__main__':
    length = 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))
    start = time.time()

    for target in sorted_list:
        naive_search(sorted_list, target)

    end = time.time()
    print("Naive Search = ", (end-start)/length)

    start = time.time()

    for target in sorted_list:
        binary_search(sorted_list, target)

    end = time.time()
    print("Binary Search = ", (end-start)/length)
