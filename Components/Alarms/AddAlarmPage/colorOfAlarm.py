from Components.Alarms.AddAlarmPage.alarmConfiguration import Configuration
from tkinter import Frame, Label


class ColorOfAlarm:
    
    frame = None
    colorFrame = None
    configuration = None
        
    def __init__(self, frame):
        
        self.frame = frame
        self.configuration = Configuration()
        self.CreateFrame()
        print("init col")
        
    def CreateFrame(self):
        
        self.colorFrame = Frame(self.frame, bg = "white", width=300, height=100)
        self.colorFrame.place(x = 0,  y = 280)
        
        txt = Label(self.colorFrame, text = "Select color:", font=("Calibri", 18) ,bg = "white")
        txt.place(x = 0, y = 0)