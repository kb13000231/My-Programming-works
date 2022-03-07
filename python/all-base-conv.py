print('You can use this program to change a number in any base (2 to 36) to any other base.')

z = '0123456789abcdefghijklmnopqrstuvwxyz'
inv_dd = dict()
for i in range(len(z)):
    inv_dd[z[i]] = inv_dd.get(z[i], 0) + i


def converter(no, base, obase):
    global z
    global inv_dd
    num = 0

    for i in range(len(no)):
        num += (base**i)*inv_dd[no[-i-1]]

    a = ''
    dd = {v: k for k, v in inv_dd.items()}
    while num > 0:
        a = dd[num % obase] + a
        num = num//obase
    return a


def inpcheck(no, base):
    for i in no:
        if i not in z[:int(base)]:
            return 0
    return 1


while True:
    inp_no = input('Please Enter your number or "done" if you want to exit: ')
    if inp_no == 'done':
        break

    print('Please Enter your input base: ', end='')
    while True:
        inp_base = input()
        try:
            int(inp_base)
            break
        except Exception:
            print('Invalid Input. Please enter an input in 2 to 36 range: ', end='')

    if inpcheck(inp_no, inp_base) == 0:
        print('Invalid Number for the given base')
        continue

    print('Please Enter your otuput base: ', end='')
    while True:
        out_base = input()
        try:
            int(out_base)
            break
        except Exception:
            print('Invalid Input. Please enter an input in 2 to 36 range: ', end='')

    print(converter(inp_no, int(inp_base), int(out_base)))
