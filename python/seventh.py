fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
else:
    fh = open(fname)
    count = 0
    for line in fh:
        if line.startswith('From:'):
            continue
        elif line.startswith('From'):
            x = line.split()
            print(x[1])
            count += 1
        else:
            continue

print("There were", count, "lines in the file with From as the first word")
