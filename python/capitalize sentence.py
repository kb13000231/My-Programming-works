def capital(s):
    s = s.split(' ')
    s = ' '.join((word.capitalize() for word in s))
    return s


print(capital(input()))
