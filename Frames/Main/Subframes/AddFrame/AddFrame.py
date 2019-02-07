from Frames.Main.Subframes.AddFrame.More.More import *
from tkinter import *
from Algorithm.SQLite_Algorithm import *

"""
The add frame will give the user the chance to add the task which he wishes to add/
The add frame itself contains many diffrent frames, which you can find in the More folder.\
So literary this frame includes two things: a "More" frame that has the things that the user
is going to enter the stuff he wishes to enter and a button called "Done".
This button will call the function end which will call the function called "insert_work" from
the SQLite_Algorithm library. The arguments for this function are going to be functions that
return the name, the points, etc. that the user entered from the other frames inside the
More frame.
#Eficient_but_complicated!!!S
"""

def add_frame(frame):

    def end(root):
        insert_work(return_name(), return_repeat(), return_points(), return_from_hour(),
                    return_from_min(), return_to_hour(), return_to_min(), return_date(),
                    'Work')                                                                                                                                                      
        root.pack_forget()
        root.destroy

    root = Frame(frame, bg='white')
    root.pack()

    x = 2

    More = Frame(root, bg = 'white')
    More.grid(row=1)

    more(More)

    Done = Button(root, text='Done', borderwidth=0, command=lambda: end(root), bg='white')
    Done.grid(row=3, sticky=W)

