from Frames.Main.Subframes.AddFrame.More.Name.Name import *
from Frames.Main.Subframes.AddFrame.More.Date.Date import *
from Frames.Main.Subframes.AddFrame.More.Repeat.Repeat import *
from Frames.Main.Subframes.AddFrame.More.Time.Time import *
from Frames.Main.Subframes.AddFrame.More.Points.Points import *
from Frames.Main.Subframes.AddFrame.AddFrame import *

"""
This is the big and mighty more frame, which, sarcastically enough, includes more frames :P
So what this frame does is combine all underlying frames together in a bundle, so that the
add frame can look neat. This frame also imported all functions that the add frame
will need in order to pass the things that the user wrote in the db.
#OrganizationMakesLifeEasier
"""

x = 2


def more(frame):

    global x
    x+=1
    Name = Frame(frame, bg='white')
    Name.grid(row=x, sticky=W)
    name(Name)
    x+=1
    date_frame = Frame(frame)
    date = tk.Button(date_frame, text='Date',command=popup, borderwidth=0, bg='white')
    date.grid(row=0, sticky=W)
    today = tk.Button(date_frame, text='Today',command=today_date(), borderwidth=0, bg='white')
    today.grid(row=0, column=1, sticky=W)
    date_frame.grid(row=x, sticky=W)
    x+=1
    Time = Frame(frame, bg='white')
    Time.grid(row=x, sticky=W)
    time(Time)
    x+=1
    Repeat = Frame(frame, bg='white')
    Repeat.grid(row=x, sticky=W)
    repeat(Repeat)
    x+=1
    Points = Frame(frame, bg='white')
    Points.grid(row=x, sticky=W)
    points(Points)

    
    
        
