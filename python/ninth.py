fname = input("Enter file name: ")
ls = list()
dd = dict()
if len(fname) < 1 :
    fname = "mbox-short.txt"
else:
    fh = open(fname)
    count = dict()
    for line in fh:
        if line.startswith('From:'):
            continue
        elif line.startswith('From'):
            x = line.split()
            y = x[5].split(':')
            ls.append(y[0])

for i in range(len(ls)):
    keys = dd.keys()
    values = dd.values()
    if ls[i] not in dd.keys():
         dd[ls[i]] = dd.get(ls[i],0) + 1
    else :
        dd[ls[i]] += 1
for k,v in sorted(dd.items()):
    print(k,v)
