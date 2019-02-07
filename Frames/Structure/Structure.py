from tkinter import *
from Frames.Main.Main import *

"""
This Frame will include buttons for the days of the week and for the projects the user has set
"""


def create_structure(parent):
    Today = Button(parent, text='Today', borderwidth=0, command=lambda: create_today_frame(return_frame())).pack(side=TOP, padx=2, pady=2)
    Organize = Button(parent, text='Organize', borderwidth=0, command=lambda: create_organize_frame(return_frame())).pack(side=BOTTOM, padx=2, pady=2)
    
