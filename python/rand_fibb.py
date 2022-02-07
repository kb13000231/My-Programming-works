import random, math

def rand_fib(n):
    k = []
    for i in range(100):
        a = 1
        b = 1

        for j in range(n):
            z = random.randint(0,1)
            if z == 0:
                c = a - b
            else:
                c = a + b
            a = b
            b = c
        k.append(int(math.log(abs(c),10)))
    return k

inp_no = int(input('Enter the number: '))
print(rand_fib(inp_no))
