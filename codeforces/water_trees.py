for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    tall = max(arr)
    days1 = 0
    days2 = 1
    for i in arr:
        days2 = (tall-i)//2
        days1 = (tall-i) % 2
    k = days2-days1
    if k % 3 == 0:
        m = k//3
        days2 -= m
        days1 += 2*m
    elif k % 3 == 1:

