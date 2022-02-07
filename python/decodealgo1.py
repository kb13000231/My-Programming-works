def alpha_check(inp_alp):
    dd = dict()
    for i in range(len(inp_alp)):
        if inp_alp[i] not in dd.keys():
            dd[inp_alp[i]] = dd.get(inp_alp[i],0) + 1
        else:
            dd[inp_alp[i]] += 1

    for k,v in dd.items():
        if v >1:
            return 0
    return 1

def str_check(inp_str):
    for i in inp_str:
        if i in inp_alp or i == ' ':
            continue
        else:
            return 0
    return 1

def decode_algo(inp_str):
    ls = list()
    for i in inp_str:
        if i == ' ':
            ls.append(' ')
        else:
            ind = inp_alp.find(i)
            if (ind-1)%2 == 0:
                a = (ind-1)/2
                ls.append(inp_alp[int(a)])
            else:
                a = (len(inp_alp)+ind+1)/2
                ls.append(inp_alp[int(a)])

    m = ''
    for j in ls:
        m += j
    return m


while True:
    inp_alp = input('Please write the alphabet used for encoding press "n" if default alphabet was\nused or "done" if completed:')
    if inp_alp == 'n':
        inp_alp_alt = input('If you want to use 0-z or the 0-9a-zA-Z,. \ntype 1 for first 2 for second: ')
        if inp_alp_alt == '1':
            inp_alp = '0123456789abcdefghijklmnopqrstuvwxyz'
        else:
            inp_alp = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.'

    elif inp_alp == 'done':
        break
    if alpha_check(inp_alp) == 0:
        print('\nInvalid alphabet: Repeating letter detected')
        continue

    inp_str = input('\nPlease enter the encoded string, if it is a file type "file" or "done" if completed: ')
    if inp_str == 'done':
        break
    elif inp_str == 'file':
        fname = input('\nType the name of the encoded file: ')
        ofile = open(fname,'r')
        out_file = ofile.read()
        check = input('\nWhat type of output do you want a "file" or plain "text": ')
        if check == 'text':
            print(decode_algo(out_file))
        else:
            fname_2 = input('\nEnter the output file name: ')
            wfile = open(fname_2,'w')
            wfile.write(decode_algo(out_file))
    else:
        if str_check(inp_str) == 0:
            print('Presented string contains a letter that is not in alphabet')
            continue
        print('The original string was', decode_algo(inp_str))
