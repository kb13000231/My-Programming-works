from itertools import combinations


def midpoint(x, y):
    return ((x[0]+y[0])/2, (x[1]+y[1])/2)


def per_slope(x, y):
    if x[1] - y[1] != 0:
        psl = (x[0]-y[0])/(x[1]-y[1])
    else:
        psl = float('inf')
    return psl


def slope(psl):
    return 1/psl if psl != 0 else float('inf')


def colineandantipodal(x, y, z):
    psl = per_slope(x, y)
    sl = slope(psl)
    pt = midpoint(x, y)

    # check collinear
    if sl == float('inf'):
        if z[0] == x[0]:
            # print('coline', 'y para')
            return False
    else:
        if z[1] == sl*z[0] + pt[1]-sl*pt[0]:
            # print('coline', 'linear')
            return False

    psl2 = per_slope(z, y)
    pt2 = midpoint(y, z)
    sl2 = slope(per_slope(pt, pt2))
    if abs(psl2) == abs(sl2):
        return True
    # print('nonequal', psl2, sl2)
    return False


for _ in range(int(input())):
    lst = []
    for i in range(int(input())):
        lst.append(list(map(int, input().split())))
    comb = combinations(lst, 3)

    coun = 0
    for i in comb:
        if colineandantipodal(i[0], i[1], i[2]):
            coun += 1
        if colineandantipodal(i[1], i[2], i[0]):
            coun += 1
        if colineandantipodal(i[0], i[2], i[1]):
            coun += 1
    print(coun)
