x = int(input())
def binary(n):
    a = ''
    global x
    if n == 0:
        a = '0'
    while n>0:
        a = str(n%2) + a
        n = n//2
    print(a.rjust(x ,'0'))

def binary_string(i):
    global x
    if i < 2**x:
        binary(i)
        binary_string(i+1)
    else:
        return 0

binary_string(0)


#for i in range(2**n):
#    binary(i)
