import random

DEF_ALPHA = [chr(i) for i in range(33, 127)]


def password(n, length):
    for i in range(n):
        a = ''
        for j in range(length):
            a += random.choice(DEF_ALPHA)
        print(a)


print('Welcome to password generator!')
n = int(input('The number of passwords required: '))
length = int(input('Length of the required passwords: '))

password(n, length)
