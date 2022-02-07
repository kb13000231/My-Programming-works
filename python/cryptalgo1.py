def encoder(a):
    ls = list(a)
    for i in range(len(ls)):
        if ls[i] not in inp_alp:
            continue
        else:
            x = inp_alp.find(ls[i])
            m = 2*(x+1)
            if m <= len(inp_alp):
                ls[i] = inp_alp[m-1]
            else:
                b = m - 2*(len(inp_alp)//2) - 2
                ls[i] = inp_alp[b]
    out = ''.join(ls)

    return out


while True:
    print('Do you want to use your own alphabet for encoding or the default base.')
    inp_alp_bool = input('Type "y" to type your own alphabet, "n" to choose the default one and "done" if completed: ')

    if inp_alp_bool == 'y':
        inp_alp = input('Please enter the alphabet: ')

    elif inp_alp_bool == 'done':
        break

    elif inp_alp_bool == 'n':
        inp_alp_alt = input('If you want to use 0-z or the 0-9a-zA-Z,. \ntype 1 for first 2 for second: ')
        if inp_alp_alt == '1':
            inp_alp = '0123456789abcdefghijklmnopqrstuvwxyz'
        else:
            inp_alp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.'
    else:
        print('Incorrect response please type y, n or done')
        continue

    inp_str = input("Do you want to encode a string(continue with your string) or an entire file(type 'file'):")

    if inp_str == 'done':
        break

    elif inp_str == 'file':
        fname = input('Please Enter the name of the file you want to encode: ')
        oname = input('Input the file name to which you want to output: ')
        s = open(fname)
        a = s.read()
        ofile = open(oname, 'w')
        ofile.write(encoder(a))
        ofile.close()

    else:
        print(encoder(inp_str))
