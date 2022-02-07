print("This program is used for converting numbers from\nbase 10 to any base from 2 to 36.\nEnter done when you're done with this program\n")

while True:
    inp_no = input('Please Enter your number: ')
    # checking for invalid cases and doing error prevention
    try:
        int(inp_no)
        while True:
            base_change = input('Please Enter the base you want to convert your number to: ')
            try:
                int(base_change)
                break
            except:
                if base_change == 'done':
                    break
                else:
                    print('Invalid Input')
                    continue

    except:
        if inp_no == 'done':
            break
        else:
            print('Invalid Input')
            continue

# defining the variables that are going to be used
    x = int(inp_no)
    y = int(base_change)
    a = ''
    z = '0123456789abcdefghijklmnopqrstuvwxyz'
    inv_dd = dict()

    for i in range(len(z)):
        inv_dd[z[i]] = inv_dd.get(z[i], 0) + i

    dd = {v: k for k, v in inv_dd.items()}

    while x > 0:
        a = dd[x % y] + a
        x = x//y
    print(inp_no, 'is', a, 'in base', base_change)
