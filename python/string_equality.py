n = 0


def check(a, b):
    global n
    if len(a) != len(b):
        return False
    elif len(a) - n == 0:
        return True
    elif a[len(a)-n-1] != b[len(b)-n-1]:
        return False
    else:
        n += 1
        return check(a, b)


x, y = input(), input()
print(check(x, y))

# power recursive
b = 1


def power(a, x):
    global b
    if x == 0:
        return 1
    else:
        return a*power(a, x-1)


a, x = input(), input()
print(power(a, x))
