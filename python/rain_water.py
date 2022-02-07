def rain_water(ls):
    ans = 0
    for i in range(len(ls)):
        ans += min(left_max(ls,i),right_max(ls,i))-ls[i]
    return ans

def left_max(ls,i):
    lm = 0
    for j in range(i+1):
        lm = max(lm,ls[j])
    return lm

def right_max(ls,i):
    rm = 0
    for j in range(i,len(ls)):
        rm = max(rm,ls[j])
    return rm

ls = [5,3,1,0,4,0,6,2,4]

print(rain_water(ls))
