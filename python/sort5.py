def is_even(p):
    min_no = p[0]
    ls = list()
    s = 0
    while len(p)>0:
        for i in range(len(p)):
            if p[i]<=p[0]:
                tmp = p[0]
                p[0] = p[i]
                p[i] = tmp
                s += 1
        ls.append(p[0])
        p.remove(p[0])
    return bool(s%2),ls

p = [3,2,0,1]
print(is_even(p))
