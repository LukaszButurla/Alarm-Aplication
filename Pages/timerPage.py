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

    def ShowTimerFrame(self):

        self.frame.tkraise()
