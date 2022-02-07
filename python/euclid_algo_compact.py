def gcd(a,b):
    assert a>=b and b>= 0 and a+b>0
    return gcd(b,a%b) if b>0 else a
