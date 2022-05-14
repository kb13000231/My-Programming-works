for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n-1 <= arr[-1] - arr[0] <= n+1:
        print("YES")
    else:
        print("NO")
