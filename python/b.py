def pre(N):
    if N>0:
        return pre(N-1) + ' ' + str(N)
    elif N == 1:
        return str(1)

#Complete this function
def printNos(N):
    #Your code here
    print(pre(N))

T = int(input())

while T>0:
    N = int(input())
    printNos(N)
    #print(printNos(N))
    T -= 1
