from tkinter import Label, Button, Frame
from Components.Alarms.CallPage.alarmInformation import AlarmInformation
from Components.Alarms.CallPage.btnOk import BtnOk

class CallPage:
    
    frame = None
    alarmPage = None
    callFrame = None
    alarmInformation = None
    menu = None
    list = None
    btnOk = None
    
    def __init__(self, frame, alarmPage, menu, list):
        
        self.frame = frame
        self.alarmPage = alarmPage
        self.menu = menu
        self.list = list
        self.CreateFrame()
        self.alarmInformation = AlarmInformation(self.callFrame)
        self.btnOk = BtnOk(self.alarmPage, self.callFrame, self.menu, self.list)
        
    def CreateFrame(self):
        
        self.callFrame = Frame(self.frame, width=300, height=550, bg = "white")
        
    def ShowCallFrame(self, alarm):
                
        self.callFrame.place(x = 0, y = 0)
        self.alarmInformation.ShowInformation(alarm)
        self.callFrame.tkraise()
        