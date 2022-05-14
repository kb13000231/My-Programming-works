# cook your dish here
from collections import Counter as ct

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = ct(arr)
    if freq.get(1, 0) == n or freq.get(-1, 0) == n:
        print('No')
    elif abs(freq.get(1, 0) - freq.get(-1, 0)) > 2:
        print('No')
    else:
        print('Yes')
