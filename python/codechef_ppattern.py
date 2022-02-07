t = int(input())
n = int(input())

for k in range(t):
    for i in range(n):
        a = ''
        for j in range(n):
            b = n*i + j + 1
            a += str(b) + ' '
        print(a)
