#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from main import main

root = Tk()
root.title('TIP AUDITS')

mainframe = ttk.Frame(root, padding='5 5 20 20')
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
ttk.Button(mainframe, text='Run Audits',command=main).grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()