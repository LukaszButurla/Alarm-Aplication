from tkinter import Label

class HourOfAlarm:
    
    frame = None
    hourLabel = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.CreateHourLabel()
        
    def CreateHourLabel(self):
        
        self.hourLabel = Label(self.frame, text = "00:00", font=("Calibri", 50), anchor="nw")
        self.hourLabel.place(x = 80, y = 70)
        
    def EditLabel(self, hour, minute):
        
        self.hourLabel.configure(text = "{}:{}".format(hour, minute))