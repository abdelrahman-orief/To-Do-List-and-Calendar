from tkinter import *
from Algorithm.Functions import *

def todo(frame):

    def extra_points(frame, where, points, number):
        p = strainer('points', 'Type', 'Points')
        edit('points', int(p[0][0])+int(points), 'Type', 'Points')
        l=strainer('', 'Number', number)
        if 1 in [int(l[0][1]), int(l[0][2]), int(l[0][3]), int(l[0][4]), int(l[0][5]), int(l[0][6]), int(l[0][7])]:
            edit('status', 1, 'Number', number)
        else:
            delete('Number', number)
        for widget in frame.winfo_children():
            widget.destroy()
        todo(frame)

        
    info = info_todo()
    x = 0

            
    for i in info:
        reward = IntVar()
        Name = Checkbutton(frame, text=i[0], variable=reward, command=lambda points=i[3], number=i[4]: extra_points(frame, 'Todo', points, number), bg='white')
        Name.grid(row=x, column=0, padx=10, sticky=W)

        Date = Label(frame, text=i[1], bg='white')
        Date.grid(row=x, column=2, padx=10, sticky=W)

        Rep = Label(frame, text=i[2], bg='white')
        Rep.grid(row=x, column=3, padx=10, sticky=W)

        Points = Label(frame, text=i[3], bg='white')
        Points.grid(row=x, column=4, padx=10, sticky=W)

        x+=1

