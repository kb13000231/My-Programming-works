def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a

  return max(a, b)

def extended_gcd(a, n):
  assert a >= n and n >= 0 and a + n > 0
  if n == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(n, a % n)
    x = q
    y = p - q * (a // n)

  assert a % d == 0 and n % d == 0
  assert d == a * x + n * y
  return (d, x, y)

def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1
    if a>=n:
        d,s,t = extended_gcd(a,n)
    else:
        d,t,s = extended_gcd(n,a)
    m = s%n
    print(m,d,s,t)
    return (b*m)%n

print(divide(1,1,2))
