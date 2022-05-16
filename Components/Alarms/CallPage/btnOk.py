from functools import partial
from tkinter import Button

class BtnOk:
    
    alarmFrame = None    
    frame = None
    menu = None
    list = None
    btnOk = None
    
    def __init__(self, alarmFrame, frame, menu, list):
        
        self.alarmFrame = alarmFrame
        self.frame = frame
        self.menu = menu
        self.list = list
        
    def CreateButton(self, alarm):
        
        self.btnOk = Button(self.frame, text = "OK", bg = "white", command=partial(self.CloseFrame, alarm))
        self.btnOk.place(x = 110, y = 500, height=40, width=80)
        
    def CloseFrame(self, alarm):
        
        if len(alarm.days) == 0:
            
            alarm.on = False
        
        alarm.played = False
        
        self.alarmFrame.tkraise()
        self.menu.tkraise()
        self.list.ShowAlarms()