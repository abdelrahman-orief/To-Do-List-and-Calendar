from tkinter import *

from_hour = 1
from_min = 1
to_hour = 1
to_min = 1

def time(frame):

    global from_hour
    global from_min
    global to_hour
    global to_min
    
    x = 0
    label1 = Label(frame, text='From: ', bg='white')
    label1.grid(row=0, column=x, sticky=W)
    x += 1
    
    from_hour = Entry(frame, bg='white')
    from_hour.grid(row=0, column=x, sticky=W)
    x += 1

    from_min = Entry(frame, bg='white')
    from_min.grid(row=0, column=x, sticky=W)
    x += 1
        
    label2 = Label(frame, text='To: ', bg='white')
    label2.grid(row=0, column=x, sticky=W)
    x += 1
    
    to_hour = Entry(frame, bg='white')
    to_hour.grid(row=0, column=x, sticky=W)
    x += 1

    to_min = Entry(frame, bg='white')
    to_min.grid(row=0, column=x, sticky=W)
    x += 1

def return_from_hour():
    return str(from_hour.get()).zfill(2)

def return_from_min():
    return str(from_min.get()).zfill(2)

def return_to_hour():
    return str(to_hour.get()).zfill(2)

def return_to_min():
    return str(to_min.get()).zfill(2)
