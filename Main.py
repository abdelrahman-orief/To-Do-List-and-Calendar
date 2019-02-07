import Frames
from Frames.Main.Main import *
from Frames.Structure.Structure import *
from Frames.Tabs.Tabs import *
from Frames.Toolbar.Toolbar import *


root = Tk() #build a window

create_table() #create a table in the database
"""
put frames in the window and insert the frames
from the Frames folder using  create_xxx(xxx)
and then packing the Frames in the place we want to
"""
toolbar = Frame(root)

create_toolbar(toolbar)

toolbar.pack(side=TOP, fill=X)

TabsFrame = Frame(root)

create_tabs(TabsFrame)

TabsFrame.pack(side=TOP, fill=X)

OverViewFrame = Frame(root)

create_structure(OverViewFrame)

OverViewFrame.pack(side=LEFT, fill=Y)

MainFrame = Frame(root)

create_main_frame(MainFrame)

MainFrame.pack(fill=BOTH, side=TOP)


root.mainloop()
