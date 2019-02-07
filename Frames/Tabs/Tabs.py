from tkinter import *
from Frames.Main.Main import *

"""
This Frame will include the tabs or features of the application like calendar, notes and todo list
"""


def create_tabs(parent):

    parent.columnconfigure((0,2), weight=1)
    
    tabs_button = Button(parent, text='All', borderwidth=0, command=lambda: create_all_frame(return_frame()))
    tabs_button.grid(padx=100, column=0, row=0)

    tabs_button = Button(parent, text='Calendar', borderwidth=0, command=lambda: create_calendar_frame(return_frame()))
    tabs_button.grid(padx=100, column=1, row=0)
    
    tabs_button = Button(parent, text='To do', borderwidth=0, command=lambda: create_todo_frame(return_frame()))
    tabs_button.grid(padx=100, column=2, row=0)

