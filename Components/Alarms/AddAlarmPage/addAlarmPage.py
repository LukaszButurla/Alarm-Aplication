from Components.Alarms.AddAlarmPage.buttons import Buttons
from Components.Alarms.AddAlarmPage.alarmConfiguration import Configuration
from tkinter import Frame

class AddAlarmPage:
    
    window = None
    addFrame = None
    buttons = None
    
    def __init__(self, window, page):
        
        self.frame = window
        self.CreateFrame()
        self.buttons = Buttons(self.addFrame, page)
        
    def CreateFrame(self):
        
        self.addFrame = Frame(self.window, width=350, height=550)
        
    def ShowAddFrame(self):
        
        self.addFrame.place(x = 0, y = 0)
        self.addFrame.tkraise()      