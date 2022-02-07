
def isort(ls):
    #Insertion sort
    for i in range(len(ls)):
        if i == 0:
            continue
        else:
            for j in range(i):
                if ls[i-j]<ls[i-j-1]:
                    temp = ls[i-j-1]
                    ls[i-j-1] = ls[i-j]
                    ls[i-j] = temp
                else:
                    continue
    return ls

def msort(ls):
    #Merge sort
    if len(ls)>1:
        mid = len(ls)//2
        a = ls[:mid]
        b = ls[mid:]

        msort(a)
        msort(b)

        i = j = k = 0
        while i < len(a) and j < len(b):
            if a[i]<b[j]:
                ls[k] = a[i]
                i += 1
            else:
                ls[k] = b[j]
                j += 1
            k += 1

        while i < len(a):
            ls[k] = a[i]
            i+= 1
            k+= 1

        while j < len(b):
            ls[k] = b[j]
            j+= 1
            k+= 1
    return ls

def bsort(ls):
    #Bubble sort
    for j in range(len(ls)-1):
        for i in range(len(ls)-1-j):
            if ls[i]>ls[i+1]:
                tmp = ls[i+1]
                ls[i+1] = ls[i]
                ls[i] = tmp
            else:
                continue
    return ls

#def qsort(ls):
    #Quick sort
#    if len(ls)>1:
#        pivot = ls[-1]
#        a = list()
#        b = list()
#        for i in ls:
#            if i <pivot:
#                a.append(i)
#            else:
#                b.append(i)
#        print(a,b)
        #qsort(a)
        #qsort(b)
#    return ls

#def rsort(ls):
    #Radix sort

#def hsort(ls):
    #Heap sort

#a = [3,5,2,18,11,6,1,15,12,17,7]
#print(qsort(a))
