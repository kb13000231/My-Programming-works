for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    coun = 0
    loc = 0
    ls = []
    gap = 0
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            loc += 1
        else:
            if loc > 1:
                coun += loc//2
            else:
                coun += loc
            loc = 0
    coun += loc//2 if loc > 1 else loc
    print(coun)
