from tkinter import *
from Algorithm.SQLite_Algorithm import *
from Frames.Main.Subframes.Rewards.See_reward.See_reward import *

def Add_reward(frame):

    global Name
    name_frame = Frame(frame, bg='white')
    name_frame.grid(row=0, column=0, sticky=W)
    name = Label(name_frame, text='Name', bg='white')
    name.pack(side=LEFT)
    Name = Entry(name_frame)
    Name.pack(side=LEFT)
    
    global Slider
    Slider = Scale(frame, from_=0, to=100, orient=HORIZONTAL, tickinterval=5, length=500, bg='white')
    Slider.set(50)
    Slider.grid(row=1, sticky=W)

    Done = Button(frame, text='Done', borderwidth=0, command=lambda: end(frame, Name.get(), Slider.get()), bg='white')
    Done.grid(row=2, column=0, sticky=W)

def end(frame, name, points):
        insert_reward(name, points, 'Reward')
        for widget in frame.winfo_children():
            widget.destroy()
