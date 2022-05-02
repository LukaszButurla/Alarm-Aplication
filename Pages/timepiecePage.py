from tkinter import Frame, Label

class TimepiecePage:

    window = None
    frame = None

    def __init__(self, root):

        self.window = root
        self.CreateTimepiecePage()

    def CreateTimepiecePage(self):

        self.frame = Frame(self.window, height=490, width=350, bg = "gray")
        self.frame.place(x = 0, y = 0)

    def ShowTimepieceFrame(self):

        self.frame.tkraise()