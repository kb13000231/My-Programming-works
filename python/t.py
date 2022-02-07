from math import pi,e

l = []
f = open('pi.csv','w')
for i in range(1,334):
    for j in range(int(i*3),int(i*3.2)+1):
        dif = abs((j/i)-pi)
        if dif < 0.01 and dif not in l:
            l.append(dif)
            f.write('{},{},{}\n'.format(j,i,dif))

a = []
g = open('e.csv','w')
for i in range(1,400):
    for j in range(int(i*2.7),int(i*2.8)+1):
        dif = abs((j/i)-e)
        if dif < 0.01 and dif not in a:
            a.append(dif)
            g.write('{},{},{}\n'.format(j,i,dif))
