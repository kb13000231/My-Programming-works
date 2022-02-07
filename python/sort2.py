def is_even(p):
    a = 0
    for i in range(len(p)-1):
        if p[i]>p[i+1]:
            t = p[i]
            p[i] = p[i+1]
            p[i+1] = t
            a += 1
            print(p,'f')
            for j in range(i+1):
                if p[j]>p[j+1]:
                    t = p[j]
                    p[j] = p[j+1]
                    p[j+1] = t
                    a += 1
                    print(p,'s',i)
                else:
                    continue
        else:
            continue
    if a%2 == 0:
        return True,a
    else:
        return False,a
p = [0,6,11,8,10,3,2,17,9,5,4,14,7,1,12]
z = [6, 2, 1, 0, 4, 5, 3]
k = [0,1,3,2]
print(is_even(z),z)#is_even(k))
