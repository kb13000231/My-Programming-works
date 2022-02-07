fname = input("Enter file name: ")
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
            count[x[1]] = count.get(x[1],0) + 1

maxname = None
maxcount = 0
for name, c in count.items():
   if maxname == None or maxcount<c :
      maxname = name
      maxcount = c
print(maxname, maxcount,count.items())
