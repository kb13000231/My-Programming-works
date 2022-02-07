def is_even(p):
    ls = list()
    c = 1
    for i in range(len(p)):
        ls.append(p[i])
        for j in range(1,len(ls)):
            while ls[j]<ls[j-1]:
                if j==0:
                    break
                else:
                    tmp = ls[j]
                    ls[j] = ls[j-1]
                    ls[j-1] = tmp
                    j = j-1
                    c = 1 - c
    return bool(c),ls
p = [0,6,11,8,10,3,2,17,9,5,4,14,7,1,12]
print(is_even(p))
