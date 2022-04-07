import heapq


def kthlargestnaive(arr, k):
    if len(arr) < k:
        return None
    while k > 1:
        del arr[arr.index(max(arr))]
        k -= 1
    return max(arr)


def kthlargest(arr, k):
    # Time O(nlogn)
    # Space 0(1)
    if len(arr) < k:
        return None
    arr.sort()
    return arr[-k]


def kthlargestheap(arr, k):
    # Time O(n + klogn)
    # Space 0(n)
    if len(arr) < k:
        return None
    arr = [-i for i in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)


lst = [1, 2, 5, 3, 5, 6, 8, 120, 24, 56]
print(kthlargestnaive(lst, 4))
