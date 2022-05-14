for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    ans = 0
    arr.sort()

    tot = 0
    for i in range(n):
        if tot + arr[i] <= x:
            tot += arr[i]
            ans += (x-tot)//(i+1) + 1
        else:
            break
    print(ans)
