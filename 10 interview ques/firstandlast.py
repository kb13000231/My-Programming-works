def firstandlast(arr, a):
    # Using linear search
    start = None
    end = 0
    for i in range(len(arr)):
        if arr[i] == a:
            if start is None:
                start = i
            elif i == len(arr)-1 or arr[i+1] > a:
                end = i
                break
    return start, end


def firstandlastopt(arr, a):
    # Using binary search
    if len(arr) == 0 or arr[0] > a or arr[-1] < a:
        return -1

    def find_start(arr, a):
        if arr[0] == a:
            return 0
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == a and arr[mid - 1] < a:
                return mid
            elif arr[mid] < a:
                left = mid + 1
            else:
                right = mid-1
        return -1

    def find_end(arr, a):
        if arr[-1] == a:
            return len(arr) - 1
        left, right = 0, len(arr)-1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == a and arr[mid+1] > a:
                return mid
            elif arr[mid] > a:
                right = mid-1
            else:
                left = mid+1
        return -1

    return find_start(arr, a), find_end(arr, a)


ls = [1, 4, 5, 5, 5, 5]
print(firstandlastopt(ls, 6))
