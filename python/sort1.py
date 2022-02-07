def is_even(p):
    a = 0
    s = 0

    while s<len(p) - 1:
        u = s
        t = u
        while u<len(p) - 1:
            u = u + 1
            if p[u] < p[t]:
                t = u
                a += 1
        tmp = p[s]
        p[s] = p[t]
        p[t] = tmp
        a += 1
        s = s + 1
    if a%2 == 0:
        return True
    else:
        return False

p = [0,6,11,8,10,3,2,17,9,5,4,14,7,1,12]
z = [9, 2, 4, 3, 8, 1, 6, 5, 0, 7]
k = [0,1,3,2]
print(is_even(z),z)#is_even(k))
