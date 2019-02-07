from tkinter import *
from Frames.Main.Main import *

"""
This Frame will always be at the top. It includes buttons for Settings, Points, Profile, Add and Notification
"""


def create_toolbar(parent):

    parent.config(bg='red')
    
    program_name = Label(parent, text='Best Application :)', bg='red')
    program_name.pack(side=LEFT, padx=2, pady=2)

    for i in ('Settings', 'Profile'):
        toolbar_button = Button(parent, bg='red', text=i, borderwidth=0)
        toolbar_button.pack(side=RIGHT, padx=20, pady=10)

    Reward = Button(parent, text='Reward',command=lambda: create_see_reward_frame(return_frame()), bg='red', borderwidth=0)
    Reward.pack(side=RIGHT, padx=20, pady=10)

    Add = Button(parent, text='Add',command=lambda: create_add_frame(return_frame()), bg='red', borderwidth=0)
    Add.pack(side=RIGHT, padx=20, pady=10)
