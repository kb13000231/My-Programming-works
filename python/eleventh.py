import re

fname = open('regex_sum_447732.txt')
y = 0
for line in fname:
    x = re.findall('[0-9]+', line)
    for i in x:
        y += int(i)
print(y)
