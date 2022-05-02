from tkinter import Button, Label, Frame

class TimerPage:

    window = None
    frame = None

    def __init__(self, root):

        self.window = root
        self.CreateTimerFrame()

    def CreateTimerFrame(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "brown")
        self.frame.place(x = 0, y = 0)   

    def ShowTimerFrame(self):

        self.frame.tkraise()
