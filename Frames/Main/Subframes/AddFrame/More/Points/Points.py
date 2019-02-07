from tkinter import *

Slider = 1

def points(frame):
    
    global Slider
    Slider = Scale(frame, from_=1, to=5, orient=HORIZONTAL, tickinterval=1, length=550, bg='white')
    Slider.set(3)
    Slider.pack()

def return_points():
    return Slider.get()
