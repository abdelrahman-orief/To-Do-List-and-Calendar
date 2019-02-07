from Frames.Main.Subframes.Show.Calendar.Calendar import *
from Frames.Main.Subframes.Show.Todo.Todo import *

def All(frame):
    Calendar = Label(frame, text='Calendar: ', bg='white')
    Calendar.grid(row=0, column=0, sticky=W)

    c = Frame(frame, bg='white')
    c.grid(row=1, column=0, sticky=W)

    calendar(c)

    line = Label(frame, text='', bg='white')
    line.grid(row=2, column=0, sticky=W)

    Todo = Label(frame, text='Todo: ', bg='white')
    Todo.grid(row=3, column=0, sticky=W)

    t = Frame(frame, bg='white')
    t.grid(row=4, column=0, sticky=W)

    todo(t)

    

    

    
