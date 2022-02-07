print("This program is used for converting numbers from\nbase any base in [2,36] to base 10.\nEnter done when you're done with this program")

while True:
    inp_no = input('Please Enter your number: ')
    if inp_no == 'done':
        break
    base_change = input('Please Enter the base you want to convert your number from: ')
    z = '0123456789abcdefghijklmnopqrstuvwxyz'
    inv_dd = dict()
    for i in range(len(z)):
        inv_dd[z[i]] = inv_dd.get(z[i],0)  + i
    aaa = sorted(inp_no, reverse = True)
    y = int(base_change)
    while True:
        try:
            y>0
            if y > inv_dd[aaa[0]]:
                break
            else:
                print('Invalid Input: the base is too low')
                base_change = input('Please Enter the base you want to convert your number from: ')
                y = int(base_change)
        except:
            print('Invalid Input')
            continue

    a = 0
    x = inp_no[::-1]

    for i in range(len(x)):
        a += int(inv_dd[x[i]])*(y**i)
    print(inp_no,'in base',y,'is',a,'in base 10')
