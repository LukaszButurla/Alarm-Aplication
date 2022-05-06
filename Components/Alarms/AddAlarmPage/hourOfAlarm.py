
from tkinter import Label


class HourOfAlarm:
    
    frame = None
    hourLabel = None
    hour = 0
    minute = 0
    
    def __init__(self, frame):
        
        self.frame = frame
        self.CreateHourLabel()
        
    def CreateHourLabel(self):
        
        self.hourLabel = Label(self.frame, text = "00:00", font=("Calibri", 50), anchor="nw")
        self.hourLabel.place(x = 80, y = 70)