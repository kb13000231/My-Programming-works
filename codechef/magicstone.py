from math import factorial as fact

# def ncr(n, r):
#     r = min(r, n-r)
#     numer = 1
#     denom = 1
#     for i in range(n, n-r, -1):
#         numer *= i
#         denom *= n-i+1
#     return (numer // denom) % (10**9+7)


# for _ in range(int(input())):
#     n, l, r = list(map(int, input().split()))

#     k = n % 2
#     counted = {}
#     lst = []
#     for i in range(l, r+1):
#         if i % 2 != k:
#             lst.append(0)
#         else:
#             m = abs((n-i)//2)
#             lst.append(counted.get(m, ncr(n, m)))
#     print(*lst)


def power(a,  b, mod):
    x, y = 1, a
    while b > 0:
        if b % 2:
            x = (x*y) % mod
        y = (y*y) % mod
        b /= 2
    return x % mod


def modular_inverse(n, mod):
    return power(n, mod-2, mod)


def nCr(n, k, mod):
    return fact(n)*((modular_inverse(fact(k) *
                     modular_inverse(fact(n-k))) % mod)) % mod

k = nCr(150000, 24, 10**9+7)
print(k)
