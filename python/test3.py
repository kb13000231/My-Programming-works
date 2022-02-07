import sortalgo
import random

ls = list()
x = list()
for i in range(1000):
    ls.append(i+1)

for i in range(len(ls)):
    a = random.choice(ls)
    x.append(a)
    ls.remove(a)

print(sortalgo.msort(x))
