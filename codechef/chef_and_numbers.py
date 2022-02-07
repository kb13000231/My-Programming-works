inp_ls = input()
a = list()
for i in range(len(inp_ls)):
    if i == len(inp_ls)-1:
        break
    elif inp_ls[i] == inp_ls[i+1]:
        continue
    else:
        a.append(inp_ls[i])
y = sorted(a)
print(a[0])
