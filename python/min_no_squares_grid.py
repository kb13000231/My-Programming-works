# fix this code
def squares(n, m):
    assert n >= 0 and m >= 0 and n + m > 0
    a = n
    b = m
    while n > 0 and m > 0:
      if n >= m:
        n = n % m
      else:
        m = m % n
    gcd = max(n,m)
    return (a*b)/(gcd*gcd)
