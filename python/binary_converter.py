print("This is a binary converter\n Enter done when you're done")
while True:
    inp_no = input('Please Enter your number: ')
    try:
        int(inp_no)
    except:
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
