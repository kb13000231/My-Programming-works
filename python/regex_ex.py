import re

txt = "The 2 rain!@ 3 in_Spain 9"

#Check if "ain" is present at the beginning of a WORD:

w = re.findall("\s", txt)
x = re.findall("\S", txt)
y = re.findall("\w", txt)
z = re.findall("\W", txt)
mcount = 0
ncount = 0
for i in range(len(y)):
    if y[i] == x[i]:
        mcount = mcount + 1
    else:
        ncount = ncount + 1
print(mcount, ncount,w,x,y,z)

a = len(w) + len(x)
b = len(y) + len(z)

if a is b:
    print('success')
#if (x):
 # print("Yes, there is at least one match!")
#else:
  #print("No match")
