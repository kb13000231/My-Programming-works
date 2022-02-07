import re

a = open('sample-text-file.txt')
c = open('new.txt')

for line in a:
    print(type(line.split()))

#b = a.read()
#e = c.read()

#print(len(b),len(e))
