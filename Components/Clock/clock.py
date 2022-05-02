from tkinter import Label

class Clock:

    frame = None
    clockTxt = None

    def __init__(self, frame):

        self.frame = frame
        self.CreateClock()

    def CreateClock(self):

        self.clockTxt = Label(self.frame, text = "00:00", bg = "white", font=("Calibri", 30))
        self.clockTxt.place(x = 100, y = 225, width=100, height=50)
