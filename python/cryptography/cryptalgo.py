# import string

DEF_ALPHA = [chr(i) for i in range(32, 127)]


def encoder(a, inp_alp):
    ls = list(a)
    k = len(inp_alp)
    for i in range(len(ls)):
        if ls[i] not in inp_alp:
            continue
        else:
            x = inp_alp.find(ls[i])
            m = 2*(x+1)
            if m <= k:
                ls[i] = inp_alp[m-1]
            else:
                b = m - 2*(k//2) - 2
                ls[i] = inp_alp[b]
    return ''.join(ls)


while True:
    print('Do you want to use your own alphabet for encoding or the default.')
    print('Type "done" when finished')
    inp_alp_bool = input('Type "y" to type your own alphabet, "n" to choose the default one: ')

    if inp_alp_bool == 'y':
        inp_alp = input('Please enter the alphabet: ')
        if inp_alp == 'done':
            break
    elif inp_alp_bool == 'done':
        break
    elif inp_alp_bool == 'n':
        inp_alp = DEF_ALPHA
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
        ofile.write(encoder(a, inp_alp))
        ofile.close()
    else:
        print(encoder(inp_str, inp_alp))
