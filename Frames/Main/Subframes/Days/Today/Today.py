from tkinter import *
from Algorithm.Functions import *

"""
This frame is called the Today frame because it shows what you have to do today(get it?).
So here is how this frame is structured:
1. At the top we have the date of today
2. Under that we see the Calendar the events that our user has to do
3. At the end we see the todos that the user has todo
"""
def Today(frame):

    def extra_points(frame, points, number):
        print("hello")
        p = strainer('points', 'Type', 'Points')
        edit('points', int(p[0][0])+int(points), 'Type', 'Points')
        l=strainer('', 'Number', number)
        if 0 in [int(l[0][1]), int(l[0][2]), int(l[0][3]), int(l[0][4]), int(l[0][5]), int(l[0][6]), int(l[0][7])]:
            edit('status', 1, 'Number', number)
            delete_today('Number', number)
            delete('Number', number)
        else:
            delete('Number', number)
        for widget in frame.winfo_children():
            widget.destroy()
        Today(frame)

    global Date
    info = info_today()
    Name = Label(frame, text=Date, bg='white')
    Name.grid(row=0, column=0, padx=10, sticky=W)
    x = 1

    number_list = strainer('Number', 'Type', 'Today')

    for i in info[0]:

        t = (float(i[4]), )

        if t not in number_list:
            insert_today(i[0], i[1], i[2], i[3], i[4])
    """
    This next two lines are going to show the user what he has to do now
    It does this by calling a function called info_now that sees what time it is now and
    compares it to what the user has to do
    """
    
    Message = Label(frame, bg='white', text=info_now())
    Message.grid(row=x, column=0, padx=10, sticky=W)
    x+=1

    Calendar = Label(frame, text='Calendar', bg='white')
    Calendar.grid(row=x, column=0, padx=10, sticky=W)
    x += 1
    
    for i in info[0]:

        reward = IntVar()
        Name = Checkbutton(frame, text=i[0], variable=reward, command=lambda points=i[3], number=i[4] : extra_points(frame, points, number), bg='white')
        Name.grid(row=x, column=0, padx=10, sticky=W)
            
        Time = Label(frame, text=i[2], bg='white')
        Time.grid(row=x, column=2, padx=10, sticky=W)

        Rep = Label(frame, text=i[1], bg='white')
        Rep.grid(row=x, column=3, padx=10, sticky=W)

        Points = Label(frame, text=i[3], bg='white')
        Points.grid(row=x, column=4, padx=10, sticky=W)
        
        x+=1

    Free = Label(frame, text='', bg='white')
    Free.grid(row=x, column=0, padx=10, sticky=W)
    x += 1

    Todo = Label(frame, text='Todo', bg='white')
    Todo.grid(row=x, column=0, padx=10, sticky=W)
    x += 1

    for i in info[1]:

        reward = IntVar()
        Name = Checkbutton(frame, text=i[0], variable=reward, command=lambda points=i[3], number=i[4] : extra_points(frame, points, number), bg='white')
        Name.grid(row=x, column=0, padx=10, sticky=W)

        Rep = Label(frame, text=i[2], bg='white')
        Rep.grid(row=x, column=3, padx=10, sticky=W)

        Points = Label(frame, text=i[3], bg='white')
        Points.grid(row=x, column=4, padx=10, sticky=W)
        
        x+=1
