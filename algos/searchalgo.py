def linear_search(ls, target):
    for i in range(len(ls)):
        if ls[i] == target:
            return i
    return -1


def binary_search(ls, target, low=None, high=None):
    # Works only when ls is sorted
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


print(f"List index: {binary_search([1, 2, 4, 6, 8, 11], 8)}")
