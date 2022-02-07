import math

def xyz(b,d):
    if d > 0:
        return float(b*math.sqrt(1+xyz(b+1,d-1)))
    elif d == 0:
        return float(b*(b+2))
    #else:
    #    return 0

print(xyz(1,1))
#min = None
#for i in range(1,100):
#    e = abs(3-xyz(1,i))
#    if min == None:
#        min = e
#    elif e<min:
#        min = e
#        print(i)
#    else:
#        continue
