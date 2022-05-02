from tkinter import Frame, Label


class InfoPage:

    window = None
    frame = None

    def __init__(self, root):

        self.window = root
        self.CreateInfoPage()

    def CreateInfoPage(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "green")
        self.frame.place(x = 0, y = 0)

    def ShowInfoPage(self):

        self.frame.tkraise()

