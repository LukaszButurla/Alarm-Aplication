from functools import partial
from tkinter import Button

class SnoozeBtn:
    
    frame = None
    alarmFrame = None
    menuFrame = None
    list = None
    
    def __init__(self, frame, alarmFrame, menuFrame, list):
        
        self.frame = frame
        self.alarmFrame = alarmFrame
        self.menuFrame = menuFrame
        self.list = list
        
    def CreateButton(self, alarm):
        
        self.snoozeBtn = Button(self.frame, text = "Snooze", bg = "white", command = partial(self.Snooze, alarm))
        self.snoozeBtn.place(x = 110, y = 440, height=40, width=80)
        
    def Snooze(self, alarm):
        
        alarm.snoozeTime += 5
                
        self.CloseFrame()
        
        
    def CloseFrame(self):
        
        self.alarmFrame.tkraise()
        self.menuFrame.tkraise()
        self.list.ShowAlarms()
        
        