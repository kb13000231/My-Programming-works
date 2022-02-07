fname = input("Enter file name: ")
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else :
        count = count + 1
        st = line.find(':')
        num = line[st+1:st+8]
        tot +=float(num)
print("Average spam confidence:", tot/count)
