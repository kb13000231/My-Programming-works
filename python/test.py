for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    coun = 0
    for i in range(1, n-1):
        if arr[i] > arr[i+1] and arr[i] > arr[i-1]:
            coun += 1
            arr[i+1] = arr[i]
    print(coun)
    print(' '.join(list(map(str, arr))))
