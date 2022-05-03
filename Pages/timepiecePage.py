from tkinter import Frame, Label
from Components.Timepiece.timepieceTxt import TimepieceTxt

class TimepiecePage:

    timepieceTxt = None
    timepieceSliders = None
    window = None
    frame = None

    def __init__(self, root):

        self.window = root
        self.CreateTimepiecePage()
        self.timepieceTxt = TimepieceTxt(self.frame)

    def CreateTimepiecePage(self):

        self.frame = Frame(self.window, height=490, width=350, bg = "white")
        self.frame.place(x = 0, y = 0)

    def ShowTimepieceFrame(self):

        self.frame.tkraise()