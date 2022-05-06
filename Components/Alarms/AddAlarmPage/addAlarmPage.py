from Components.Alarms.AddAlarmPage.buttons import Buttons
from Components.Alarms.AddAlarmPage.alarmConfiguration import Configuration
from tkinter import Frame


class AddAlarmPage:
    
    window = None
    addFrame = None
    menuFarme = None
    buttons = None
    listOfAlarms = None
    
    def __init__(self, window, page, menuFrame, list):
        
        self.frame = window
        self.menuFarme = menuFrame
        self.listOfAlarms = list
        self.CreateFrame()
        self.buttons = Buttons(self.addFrame, page, menuFrame, self.listOfAlarms)
        
    def CreateFrame(self):
        
        self.addFrame = Frame(self.window, width=350, height=550)
        
    def ShowAddFrame(self):
        
        self.addFrame.place(x = 0, y = 0)
        self.addFrame.tkraise()      