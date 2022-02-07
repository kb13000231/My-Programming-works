t = input()
t = t.split()
n = int(t[0])
k = int(t[1])

inp = input()
inp = inp.split()

for i in range(n):
    inp[i] = int(inp[i])

a = n % k
b = n//k

x = inp[0]*inp[b-1]
for i in range(b):
    x *= inp[b + k*(i+1) - 1]

print(x % 1000000007)
