from collections import Counter


def isanagram(a, b, just_alphabets=False):
    if len(a) != len(b):
        return False
    if just_alphabets:
        a = a.lower()
        b = b.lower()
    return Counter(a) == Counter(b)


print(isanagram('nameless', 'salesmen'))
