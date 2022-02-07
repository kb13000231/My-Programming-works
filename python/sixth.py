fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    x = line.split()
    for i in range(len(x)):
        if x[i] not in lst:
            lst.append(x[i])
        else:
            continue
lst.sort()
print(lst)
