from tkinter import *

Sun = 1
Mon = 1
Tue = 1
Wed = 1
Thu = 1
Fri = 1
Sat = 1

def repeat(frame):
    global Sun
    global Mon
    global Tue
    global Wed
    global Thu
    global Fri
    global Sat

    Sun = IntVar()
    Mon = IntVar()
    Tue = IntVar()
    Wed = IntVar()
    Thu = IntVar()
    Fri = IntVar()
    Sat = IntVar()
    
    Checkbutton(frame, text='Sunday', variable=Sun, bg='white').pack(side=LEFT, padx=5)
    Checkbutton(frame, text='Monday', variable=Mon, bg='white').pack(side=LEFT, padx=5)
    Checkbutton(frame, text='Tuesday', variable=Tue, bg='white').pack(side=LEFT, padx=5)
    Checkbutton(frame, text='Wednesday', variable=Wed, bg='white').pack(side=LEFT, padx=5)
    Checkbutton(frame, text='Thursday', variable=Thu, bg='white').pack(side=LEFT, padx=5)
    Checkbutton(frame, text='Friday', variable=Fri, bg='white').pack(side=LEFT, padx=5)
    Checkbutton(frame, text='Saturday', variable=Sat, bg='white').pack(side=LEFT, padx=5)

def return_repeat():
    return [Sun.get(), Mon.get(), Tue.get(), Wed.get(), Thu.get(), Fri.get(), Sat.get()]
