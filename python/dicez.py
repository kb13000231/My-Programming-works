import random
l = 100
b = dict()
while l>0:
    a = random.randint(1,6)
    if str(a) not in b.keys():
        b[str(a)] = b.get(str(a),0) + 1
    else:
        b[str(a)] += 1
    l -= 1

for k,v in b.items():
    print(k,':', v)
