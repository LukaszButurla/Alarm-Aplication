from tkinter import Frame

class AlarmsPage:

    window = None
    frame = None

    def __init__(self, root):

        self.window = root
        self.CreateAlarmsPage()

    def CreateAlarmsPage(self):

        self.frame = Frame(self.window, height=490, width=350, bg = "red")
        self.frame.place(x = 0, y = 0)

    def ShowAlarmsPage(self):

        self.frame.tkraise()


