import math

def fibonacci_seq(n):
    if n<=1:
        return n
    else:
        a = 0
        b = 1
        c = 0
        x = []

        for i in range(2,n+1):
            c = a + b
            a = b
            x.append(b)
            b = c
        return x

def fibonacci(n):
    if n<=1:
        return n
    else:
        a = 0
        b = 1
        c = 0
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        c = str(c)
        c = c[0]+'*10' +'^'+str(int(math.log(b,10)))
        return c

def factorial(x):
    if x<=1:
        return x
    else:
        z = 1
        for i in range(2,x+1):
            z *= i
        t = z
        z = str(z)
        z = z[0] + '*10^' + str(int(math.log(t,10)))
        return z
