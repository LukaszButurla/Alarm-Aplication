from multiprocessing.connection import answer_challenge
from tkinter import Button, Label, Frame
from Components.Timer.timerBtn import TimerButtons

class TimerPage:

    window = None
    frame = None
    timerBtn = None

    def __init__(self, root):

        self.window = root
        self.CreateTimerFrame()
        self.timerBtn = TimerButtons(self.frame)

    def CreateTimerFrame(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "white")
        self.frame.place(x = 0, y = 0) 
        
        txt = Label(self.frame, text = "Timer", font=("Calibri", 25), anchor="nw", bg = "white")  
        txt.place(x = 5, y = 5, width=80, height=40)

    def ShowTimerFrame(self):

        self.frame.tkraise()
