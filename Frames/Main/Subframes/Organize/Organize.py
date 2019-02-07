from tkinter import *
from Algorithm.Functions import *

def organize(frame):

    def submit(Timelist, Infolist):
        Times = []
        for i in Timelist:
            from_hour = i[0].get().zfill(2)
            from_min = i[1].get().zfill(2)
            to_hour = i[2].get().zfill(2)
            to_min = i[3].get().zfill(2)
            Times.append('{}:{}-{}:{}'.format(from_hour, from_min, to_hour, to_min))
        z = 0
        for i in Infolist:
            if Times[z] != '00:00-00:00':
                insert_today(i[0], Times[z], i[2], i[3], i[4])
            z+=1
        for widget in frame.winfo_children():
            widget.destroy()
        organize(frame)
        
        
    info = info_today()
    x = 0
    y=0
    Timelist = []

    Calendar = Label(frame, text='Calendar', bg='white')
    Calendar.grid(row=x, column=0, padx=10, sticky=W)
    x += 1

    number_list = strainer('Number', 'Type', 'Today')

    for i in info[0]:

        t = (float(i[4]), )

        if t not in number_list:
            insert_today(i[0], i[1], i[2], i[3], i[4])

    list = strainer('', 'Type', 'Today')
    
    for l in list:
        Name = Label(frame, text=l[0], bg='white')
        Name.grid(row=x, column=0, sticky=W)

        Time = Label(frame, text=l[9], bg='white')
        Time.grid(row=x, column=1, sticky=W)

        x+=1

    Free = Label(frame, text='', bg='white')
    Free.grid(row=x, column=0, padx=10, sticky=W)
    x += 1

    Todo = Label(frame, text='Todo', bg='white')
    Todo.grid(row=x, column=0, padx=10, sticky=W)

    extra = Label(frame, text='(Please fill the time you want to do this thing at)', bg='white')
    extra.grid(row=x, column=1, columnspan=7, padx=10, sticky=W)
    x += 1

    submit_list = []

    for i in info[1]:

        if (float(i[4]), ) in number_list:
            continue

        submit_list.append(i)

        
        Name = Label(frame, text=i[0], bg='white')
        Name.grid(row=x, column=y, padx=10, sticky=W)
        y += 1

        label1 = Label(frame, text='From: ', bg='white')
        label1.grid(row=x, column=y, sticky=W)
        y += 1

        from_hour = Entry(frame, bg='white')
        from_hour.grid(row=x, column=y, sticky=W)
        y += 1

        from_min = Entry(frame, bg='white')
        from_min.grid(row=x, column=y, sticky=W)
        y += 1
        
        label2 = Label(frame, text='To: ', bg='white')
        label2.grid(row=x, column=y, sticky=W)
        y += 1
    
        to_hour = Entry(frame, bg='white')
        to_hour.grid(row=x, column=y, sticky=W)
        y += 1

        to_min = Entry(frame, bg='white')
        to_min.grid(row=x, column=y, sticky=W)
        y += 1

        Timelist.append([from_hour, from_min, to_hour, to_min])

        y = 0
        x+=1

    x+=1
    Submit = Button(frame, text='Submit', command=lambda:submit(Timelist, submit_list),bg='white')
    Submit.grid(row=x, column=0, sticky=W)


        
        
        
        
