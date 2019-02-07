from tkinter import *
from Algorithm.SQLite_Algorithm import *
from Frames.Main.Subframes.Rewards.Add_reward.Add_reward import *

def See_reward(frame):

    def create_add_reward_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()
        Add_reward(frame)

    def take_from_points(label, points, var):
        p = strainer('points', 'Type', 'Points')
        edit('points', int(p[0][0])-int(points), 'Type', 'Points')
        p = strainer('points', 'Type', 'Points')
        points = str(int(p[0][0]))
        label.configure(text=points)
        var.set(0)
    
    list = strainer('', 'Type', 'Reward')

    x = 0

    Coins = Label(frame, text="Coins: ", bg="white").grid(row=x, column=0, sticky=W)

    p = strainer('points', 'Type', 'Points')
    
    Current = Label(frame, text=str(int(p[0][0])), bg="white")
    Current.grid(row=x, column=1, sticky=W)
    x+=1

    Reward = Label(frame, text="Rewards: ", bg="white").grid(row=x, column=0, sticky=W)
    x+=1

    for l in list:
        reward = IntVar()
        Checkbutton(frame, text=l[0], variable=reward, command=lambda points=l[8], var = reward: take_from_points(Current, points, var), bg='white').grid(row=x, column=0, sticky=W)
        Points = Label(frame, text=int(l[8]), bg='white').grid(row=x, column=1, sticky=W)
        x+=1

    Add = Button(frame, text='Add reward', borderwidth=0, command=lambda: create_add_reward_frame(frame), bg='white').grid(row=x, column=0, sticky=W)
    x+=1

    
