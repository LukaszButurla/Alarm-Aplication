from tkinter import Frame, Label


class InfoPage:

    window = None
    frame = None

    def __init__(self, root):

        self.window = root
        self.CreateInfoPage()

    def CreateInfoPage(self):

        self.frame = Frame(self.window, width=350, height=490, bg = "white")
        self.frame.place(x = 0, y = 0)
        
        txtInfo = Label(self.frame, text = "Info", bg = "white", font=("Calibri", 35))
        txtInfo.place(x = 10, y = 10)
        
        txtCreator = Label(self.frame, text = "Creator: Łukasz Buturla", bg = "white", font=("Calibri", 15))
        txtCreator.place(x = 10, y = 100)

    def ShowInfoPage(self):

        self.frame.tkraise()

