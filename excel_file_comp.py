import openpyxl as op


def conv(fname):
    a = fname.split('.')
    ofname = a[0] + '.csv'
    xlsobj = op.load_workbook(fname)
    sheet = xlsobj.active
    data = sheet.rows
    ofile = open(ofname, 'w+')
    for row in data:
        dlist = list(row)
        for i in range(len(dlist)):
            if i == len(dlist) - 1:
                ofile.write(str(dlist[i].value))
            else:
                ofile.write(str(dlist[i].value) + ',')
        ofile.write('\n')
    return ofname


a = open(conv(input("First file in comparison: ")), 'r')
b = open(conv(input("Second file in comparison: ")), 'r')

c = a.readlines()
d = b.readlines()

for i in range(len(c)):
    e = c[i].split(',')
    f = d[i].split(',')
    if len(e) != len(f):
        print(e, f)
    else:
        for j in range(len(e)):
            if e[j] != f[j]:
                print(i+1, e, f)
            else:
                continue
        continue
