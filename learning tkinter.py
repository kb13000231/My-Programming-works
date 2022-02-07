import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=700, bg="#FFEE75")
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openfile = tk.Button(root, text="Open file", padx=10,
                     pady=5, fg="black", bg="#FFEE75")
openfile.pack()

root.mainloop()
