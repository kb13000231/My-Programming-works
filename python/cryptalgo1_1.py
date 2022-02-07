while True:
    print('Do you want to use your own alphabet for encoding or the default 0-z.')
    inp_alp_bool = input('Type "y" to type your own alphabet, "n" to choose the default one and "done" if completed: ')

    if inp_alp_bool == 'y':
        inp_alp = input('Please enter the alphabet: ')
    elif inp_alp_bool == 'done':
        break
    elif inp_alp_bool == 'n':
        inp_alp = '0123456789abcdefghijklmnopqrstuvwxyz'
    else:
        print('Incorrect response please type y, n or done')
        continue

    inp_str = input("Do you want to encode a string(continue with your string) or an entire file(type 'file'): ")
    if inp_str == 'done':
        break
    elif inp_str == 'file':
        fname = input('Please Enter the name of the file you want to encode: ')
        oname = input('Input the file name to which you want to output: ')
        open('out.txt', 'w')
        oname.write(file_encoder(fname))
    else:
        print(str_encoder(inp_str))
