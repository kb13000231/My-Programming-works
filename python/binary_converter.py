print("This is a binary converter\nEnter done when you're done")
while True:
    inp_no = input('Please Enter your number: ')
    try:
        int(inp_no)
    except Exception:
        if inp_no == 'done':
            break
        else:
            print('Invalid Input, Please enter a number or done')

    x = int(inp_no)
    y = 2
    a = ''

    while x > 0:
        a = str(x % y) + a
        x = x//y
    print(a)
