from tkinter import Label, Frame
from Components.Clock.clock import Clock

class ClockPage:

    window = None
    frame = None
    clock = None

    def __init__(self, root):

        self.window = root
        self.CreateClockPage()
        self.clock = Clock(self.frame)


    def CreateClockPage(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "white")
        self.frame.place(x = 0, y = 0)

    def ShowClockFrame(self):

        self.frame.tkraise()
