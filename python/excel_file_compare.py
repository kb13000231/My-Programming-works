# import pandas as pd
import openpyxl as op
import tkinter as tk
from tkinter import filedialog  # , Text
# import os

flist = []


def addexcelfile():
    filename = filedialog.askopenfilename(initialdir="/", title='Select File',
                                          filetypes=(
                                              ("Excel files", "*.xls *.xlsx"),
                                              ("All files", "*.*")))
    # print(filename)
    flist.append(filename)
    label = tk.Label(frame, text=filename, bg="gray")
    label.pack()


def conv(fname):
    x = fname.split('//')[-1]
    a = x.split('.')
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


# def save():
#     filename = filedialog.asksaveasfilename(initialdir="/",
#                                             title='Save File as',
#                                             filetypes=(
#                                                       ("Excel files",
#                                                        "*.xls *.xlsx"),
#                                                       ("All files", "*.*")))


root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=600, bg="#FFEE75")
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openfile1 = tk.Button(root, text="Select First File", padx=10, pady=5,
                      fg="black", bg="#FFEE75", command=addexcelfile)
openfile1.pack()

openfile2 = tk.Button(root, text="Select Second File", padx=10, pady=5,
                      fg="black", bg="#FFEE75", command=addexcelfile)
openfile2.pack()

root.mainloop()


a = open(conv('//'.join(flist[0].split('/'))), 'r')
b = open(conv('//'.join(flist[1].split('/'))), 'r')

c = a.readlines()
d = b.readlines()

ofile = open('',)

for i in range(max(len(c), len(d))):
    try:
        if i > len(c) - 1:
            raise ValueError
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
    except ValueError:
        print(i+1, [], d[i].split(','))
