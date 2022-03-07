# Print all binary strings of n length

def binary(x, n):
    a = ''
    if n == 0:
        a = '0'
    while n > 0:
        a = str(n % 2) + a
        n = n//2
    print(a.rjust(x, '0'))


def binary_string(x, i):
    if i < 2**x:
        binary(x, i)
        binary_string(x, i+1)
    else:
        return 0


binary_string(int(input()), 0)
