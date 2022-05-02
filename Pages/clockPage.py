from tkinter import Label, Frame

class ClockPage:

    window = None
    frame = None

    def __init__(self, root):

        self.window = root
        self.CreateClockPage()


    def CreateClockPage(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "yellow")
        self.frame.place(x = 0, y = 0)

    def ShowClockFrame(self):

        self.frame.tkraise()
