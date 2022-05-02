from tkinter import Label
from datetime import date, datetime

class Clock:

    frame = None
    clockTxt = None
    hour = None
    minute = None

    def __init__(self, frame):

        self.frame = frame
        self.CreateClock()
        self.LoadTime()
        self.ShowTime()

    def CreateClock(self):

        self.clockTxt = Label(self.frame, text = "00:00", bg = "white", font=("Calibri", 30))
        self.clockTxt.place(x = 100, y = 225, width=100, height=50)

    def LoadTime(self):

        self.hour = datetime.today().hour
        self.minute = datetime.today().minute

    def ShowTime(self):

        self.clockTxt.configure(text = "{}:{}".format(self.hour, self.minute))