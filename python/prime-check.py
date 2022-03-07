def exactly3Divisors(N):
    c = 0
    a = int(N**(1/2))
    if a >= 2:
        c = 1
        for i in range(3, a+1, 2):
            prime = 1
            b = int(i**(1/2))
            for j in range(2, b+1):
                if i % j == 0:
                    prime = 0
            if prime == 1:
                c += 1
    return c


T = int(input())

while T > 0:
    N = int(input())
    print(exactly3Divisors(N))
    T -= 1


def isprime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def exactly3Divisors(N):
    count = 0
    i = 2
    while i*i <= N:
        if isprime(i) and i**2 <= N:
            count += 1
        i += 1
    return count


def check_prime(n):
    if n % 2 == 0:
        return 'NO'
    a = int(n**(1/2))

    for i in range(2, a + 1):
        if n % i == 0:
            return 'NO'
    return 'YES'
