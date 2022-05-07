from tkinter import Button
from Components.Alarms.AddAlarmPage.alarmConfiguration import Configuration
from Components.Alarms.AddAlarmPage.hourOfAlarm import HourOfAlarm
from Components.Alarms.alarms import Alarms
from functools import partial


class Buttons:
    
    page = None
    frame = None
    menuFrame = None
    listOfAlarms = None
    hourOfAlarm = None
    addHourBtn = None
    subtractHourBtn = None
    addMinuteBtn = None
    subtractMinuteBtn = None
    cancelBtn = None
    addAlarmBtn = None
    minute = None
    hour = None
    
    def __init__(self, frame, page, menuFrame, list):
        
        self.page = page
        self.menuFrame = menuFrame
        self.listOfAlarms = list
        self.frame = frame
        self.hourOfAlarm = HourOfAlarm(self.frame)
        self.minute = Configuration.minute
        self.hour = Configuration.hour
        self.CreateButtons()
        
    def CreateButtons(self):
        
        self.addHourBtn = Button(self.frame, text = "+", command=partial(self.AddOrSubtract, "hour", 1))
        self.addHourBtn.place(x = 110, y = 60)
        
        self.subtractHourBtn = Button(self.frame, text = "-", command=partial(self.AddOrSubtract, "hour", -1))
        self.subtractHourBtn.place(x = 110, y = 150)
        
        self.addMinuteBtn = Button(self.frame, text = "+", command=partial(self.AddOrSubtract, "minute", 1))
        self.addMinuteBtn.place(x = 200, y = 60)
        
        self.subtractMinuteBtn = Button(self.frame, text = "-", command=partial(self.AddOrSubtract, "minute", -1))
        self.subtractMinuteBtn.place(x = 200, y = 150)
        
        self.cancelBtn = Button(self.frame, text = "Cancel", command = self.Cancel)
        self.cancelBtn.place(x = 20, y = 500)
        
        self.addAlarmBtn = Button(self.frame, text = "Add", command = self.AddAlarm)
        self.addAlarmBtn.place(x = 230, y = 500)
                
        
    def Cancel(self):
        
        self.hour = 0
        self.minute = 0
        
        self.hourOfAlarm.EditLabel(self.hour, self.minute)
        self.page.tkraise()
        self.menuFrame.tkraise()        
        
    def AddAlarm(self):
               
        alarm = Alarms(True, self.hour, self.minute, 3, False, "opis")
        
        self.menuFrame.tkraise()
        self.page.tkraise()
        self.listOfAlarms.ShowAlarms()                
        
        
    def AddOrSubtract(self, time, number):
        
        if time == "hour":
            
            if self.hour + number >= 0 and self.hour + number <= 23:
                
                self.hour += number
                
            elif self.hour + number < 0:
                
                self.hour = 23
                
            elif self.hour + number > 23:
                
                self.hour = 0            
            
        elif time == "minute":
            
            if self.minute + number >= 0 and self.minute + number <= 59:
                
                self.minute += number
                
            elif self.minute + number < 0:
                
                self.minute = 59
                
            elif self.minute + number > 59:
                
                self.minute = 0                     
            
        self.hourOfAlarm.EditLabel(self.hour, self.minute)
            
        
        