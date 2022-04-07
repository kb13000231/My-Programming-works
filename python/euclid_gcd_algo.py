def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


while True:
    a, b = input(), input()
    if a or b == "done":
        break
    print(gcd(int(a), int(b)))
