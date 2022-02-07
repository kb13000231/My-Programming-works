# This program is used to find colors in a given css text

import re
n = int(input())
s = ''
for i in range(n):
    s += input() + '\n'
a = re.findall('#[a-fA-F0-9]+', s)
b = re.findall('#[a-fA-F0-9]+\s*{', s)
for i in range(len(b)):
    if len(b) < 7:
        b[i] = b[i][:4]
    else:
        b[i] = b[i][:7]

for i in a:
    if len(i) == 4 or len(i) == 7:
        if i in b:
            continue
        else:
            print(i)
    else:
        continue
