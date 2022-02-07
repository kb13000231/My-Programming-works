def print_rangoli(size):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(2*size-1):
        b = ''
        if i <= (2*size-1)//2:
            b = a[size-i-1]
            c = ''
            for j in range(i):
                c += a[size-j-1] + '-'
            print((c + b + c[::-1]).center(4*size-3,'-'))
        else:
            b = a[i-size+1]
            c = ''
            for j in range(2*size - i - 2):
                c += a[size-j-1] + '-'
            print((c + b + c[::-1]).center(4*size-3,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
