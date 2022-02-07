import pandas as pd
import openpyxl as op

def conv(fname):
    a = fname.split('.')
    ofname = a[0] + '.csv'
    xlsobj = op.load_workbook(fname)
    sheet = xlsobj.active
    data = sheet.rows
    ofile = open(ofname, 'w+')
    for row in data:
        l = list(row)
        for i in range(len(l)):
            if i == len(l) - 1:
                ofile.write(str(l[i].value))
            else:
                ofile.write(str(l[i].value) + ',')
        ofile.write('\n')
    return ofname

#Test
# ifname = input('Please input the file name to convert: ')
# a = conv(ifname)
# print(a)
