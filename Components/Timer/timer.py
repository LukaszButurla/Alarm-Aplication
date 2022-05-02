from tkinter import Label

class Timer:
    
    frame = None
    timeStart = None
    timerTxt = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.ShowTimer()
        
    def ShowTimer(self):
        
        self.timerTxt = Label(self.frame, text = "00:00:00.00", font=("Calibri", 30), bg = "white")
        self.timerTxt.place(x = 50, y = 225, width=200, height=60)