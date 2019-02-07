from Frames.Main.Subframes.AddFrame.AddFrame import *
from Frames.Main.Subframes.Show.Calendar.Calendar import *
from Frames.Main.Subframes.Show.Todo.Todo import *
from Frames.Main.Subframes.Show.All import *
from Frames.Main.Subframes.Organize.Organize import *
from Frames.Main.Subframes.Days.Today.Today import *
from Frames.Main.Subframes.Rewards.See_reward.See_reward import *

"""
Will include what the user wants to see
This frame, will have many diffrent states according to what the user will click
This is why it needs to return itself and create a frame inside of itself, e.g. "create_add_frame"
Then when the user touches a button, the the button will call the frame which will include
what the user wants to see
#pretty_neat
"""

frame = 1

def create_main_frame(parent):

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), height=1000)

    global frame

    canvas=Canvas(parent, bg='white')
    frame=Frame(canvas, bg='white')
    myscrollbar=Scrollbar(parent,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    myscrollbar.pack(side="right",fill="y")
    canvas.pack(side="left", fill=BOTH, expand=YES)
    canvas.create_window((0,0),window=frame,anchor='nw')
    frame.bind("<Configure>",myfunction)

def return_frame():
    global frame
    return frame

#Here are the frames which are going to be added inside this frame

def create_add_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    add_frame(frame)

def create_calendar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    calendar(frame)

def create_todo_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    todo(frame)

def create_all_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    All(frame)

def create_today_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    Today(frame)

def create_see_reward_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    See_reward(frame)

def create_organize_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    organize(frame)
