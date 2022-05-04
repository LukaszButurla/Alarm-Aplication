from tkinter import Frame, Label
from Components.Timepiece.timepiece import TimepieceTxt
from Components.Timepiece.timepieceBtn import TimepieceButtons

class TimepiecePage:

    timepieceBtn = None
    window = None
    frame = None

    def __init__(self, root):

        self.window = root
        self.CreateTimepiecePage()
        self.timepieceBtn = TimepieceButtons(self.frame)

    def CreateTimepiecePage(self):

        self.frame = Frame(self.window, height=490, width=350, bg = "white")
        self.frame.place(x = 0, y = 0)

    def ShowTimepieceFrame(self):

        self.frame.tkraise()