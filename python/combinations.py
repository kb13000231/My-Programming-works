# A Python program to print all
# combinations of given length
from itertools import combinations
inp_no = input('Enter the num:')
# Get all combinations of [1, 2, 3]
# and length 2
x = int(inp_no)
a = 0
for i in range(int(0.4*x), int(0.6*x) + 1):
    comb = combinations(range(x), i)
    a += len(list(comb))
print(a, float(a/(2**x)))
