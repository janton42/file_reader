#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from audits import Auditor

root = Tk()
root.title('TIP AUDITS')

def all_audits():
	Auditor.active_users_without_contracts()
	Auditor.l3_locations()
	Auditor.end_dates()
	Auditor.multiple_contracts()
	Auditor.currently_whitelisted()

mainframe = ttk.Frame(root, padding='10 10 40 40')
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Weekly Audits').grid(column=1, row=0, sticky=W)
ttk.Button(mainframe, text='Run All', command=all_audits).grid(column=2, row=0, sticky=W)

ttk.Label(mainframe, text='Individual Reports').grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text='Active Users Without Contracts').grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text='Run Report', command=Auditor.active_users_without_contracts).grid(column=3, row=3, sticky=N)
ttk.Label(mainframe, text='Unnapproved Hourly ICs in L3 Locations').grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text='Run Report', command=Auditor.l3_locations).grid(column=3, row=4, sticky=N)
ttk.Label(mainframe, text='End Dates').grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text='Run Report', command=Auditor.end_dates).grid(column=3, row=5, sticky=N)
ttk.Label(mainframe, text='Freelancers with Multiple TIP Contracts').grid(column=2, row=6, sticky=W)
ttk.Button(mainframe, text='Run Report', command=Auditor.multiple_contracts).grid(column=3, row=6, sticky=N)
ttk.Label(mainframe, text='Whitelist Review and Update').grid(column=2, row=7, sticky=W)
ttk.Button(mainframe, text='Run Report', command=Auditor.currently_whitelisted).grid(column=3, row=7, sticky=N)

ttk.Label(mainframe, text='Other Reports').grid(column=4, row=0)

ttk.Label(mainframe, text='ICs with Upwork Assets').grid(column=5, row=1, sticky=W)
ttk.Button(mainframe, text='Run Report', command=Auditor.fls_with_assets).grid(column=6, row=1, sticky=N)
ttk.Label(mainframe, text='Pulse Survey Prep').grid(column=5, row=2, sticky=W)
ttk.Button(mainframe, text='Run Report', command=Auditor.survey_prep).grid(column=6, row=2, sticky=N)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


# root.mainloop()