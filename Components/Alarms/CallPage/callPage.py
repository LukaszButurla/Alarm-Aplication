from tkinter import Label, Button, Frame
from Components.Alarms.CallPage.btnOk import BtnOk

class CallPage:
    
    frame = None
    alarmPage = None
    callFrame = None
    menu = None
    btnOk = None
    
    def __init__(self, frame, alarmPage, menu):
        
        self.frame = frame
        self.alarmPage = alarmPage
        self.menu = menu
        self.CreateFrame()
        self.btnOk = BtnOk(self.alarmPage, self.callFrame, self.menu)
        
    def CreateFrame(self):
        
        self.callFrame = Frame(self.frame, width=300, height=550, bg = "white")
        
    def ShowCallFrame(self, alarm):
                
        self.callFrame.place(x = 0, y = 0)
        self.callFrame.tkraise()
        