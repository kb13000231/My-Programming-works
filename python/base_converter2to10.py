print('This program is used for converting numbers from\n base 10 to any base from 2 to 36')

while True:
    inp_no = input('Please Enter your number: ')
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
    x = int(inp_no)
    y = int(base_change)
    a = ''

    while x > 0:
        a = str(x % y) + a
        print(a)
        x = x//y
    print(inp_no, 'is', a, 'in base', base_change)
