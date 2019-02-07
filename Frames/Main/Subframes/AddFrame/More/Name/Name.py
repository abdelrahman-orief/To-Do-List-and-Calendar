from tkinter import *

name_entry = 1

def name(frame):
    global name_entry
    name = Label(frame, text='Name', bg='white')
    name.grid(row=0, column=0, sticky=W)
    name_entry = Entry(frame)
    name_entry.grid(row=0, column=1, sticky=W)

def return_name():
    return name_entry.get()
