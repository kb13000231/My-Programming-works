s = open(fname)
out = ''
for line in s:
    c = line.split()
    for j in range(len(c)):
        ls = list()
        for i in range(len(c[j])):
            ls.append(c[j][i])
            x = inp_alp.find(c[j][i])
            m = 2*(x+1)
            if m<=len(inp_alp):
                ls[i] = inp_alp[m - 1]
            else:
                a = m - 2*(len(inp_alp)//2) - 2
                ls[i] = inp_alp[a]
        for i in range(len(ls)):
            out = out + ls[i]
        if j < len(c) - 1:
            out += ' '
        else:
            out += ''

s = open(fname)
a = s.read()
ls = list(a)
for i in ls:
    if i == ' ' or i == '\n':
        continue
    else:
        x = inp_alp.find(i)
        m = 2*(x+1)
        if m <= len(inp_alp):
            i = inp_alp[m-1]
        else:
            b = m - 2*(len(inp_alp)//2) - 2
            i = inp_alp[b]
''.join(ls)
