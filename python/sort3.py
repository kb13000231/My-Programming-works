def is_even(p):
    count=0
    for i in range(len(p)):
        t=i
        for j in range(i+1,len(p)):
            if p[t]>p[j]:
                t=j
        if t!=i:
            p[i],p[t]=p[t],p[i]
        count+=1
        if count%2==0:
            return True
        else:
            return False

z = [6, 2, 1, 0, 4, 5, 3]
print(is_even(z),z)
