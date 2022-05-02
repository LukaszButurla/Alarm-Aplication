from tkinter import Button

class TimerButtons:

    frame = None
    btnStart = None
    btnStopStart = None
    BtnReset = None

    def __init__(self, frame):

        self.frame = frame
        self.CreateButtons()

    def CreateButtons(self):

        self.btnStart = Button(self.frame, text = "<")
        self.btnStopStart = Button(self.frame, text = "P")
        self.BtnReset = Button(self.frame, text = "R")
