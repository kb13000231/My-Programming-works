from itertools import product
a = [[0,1,2,3],[10,11,12,13],[20,21,22,23],[30,31,32,33]]
c = 0
r = list(product(*a))
for i in r:
    if sum(i) == 66:
        c += 1
print(c)
