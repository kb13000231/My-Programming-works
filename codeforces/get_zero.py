n = int(input())
arr = list(map(int, input().split()))
lst = []

for i in arr:
    k = 16
    for j in range(16):
        n2 = 0
        m = i+j
        while m % 2 == 0 and n2 < 15:
            m = m//2
            n2 += 1
        k = min(k, j + 15 - n2)
    lst.append(str(k))
print(' '.join(lst))
