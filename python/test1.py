a = list(map(int,input().split()))

b = [1]
for i in range(1,len(a)):
    if a[i]<a[i-1]:
        b.append(1)
    elif a[i]>a[i-1]:
        b.append(b[i-1] + 1)

print(b)
