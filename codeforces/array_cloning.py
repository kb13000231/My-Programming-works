from collections import Counter as ct

for _ in range(int(input())):
    n = int(input())
    arr = input().split()

    freq = ct(arr)
    a = ct.most_common(freq, 1)[0][1]

    opr = 0
    while a < n:
        opr += 1
        opr = opr + a if 2*a < n else opr + n - a
        a = 2*a if 2*a < n else n
    print(opr)
