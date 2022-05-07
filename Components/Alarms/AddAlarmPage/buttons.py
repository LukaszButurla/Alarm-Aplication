from tkinter import Button
import Components.Alarms.AddAlarmPage.alarmConfiguration as aC
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
    
    def __init__(self, frame, page, menuFrame, list):
        
        self.page = page
        self.menuFrame = menuFrame
        self.listOfAlarms = list
        self.frame = frame
        self.hourOfAlarm = HourOfAlarm(self.frame)
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
        
        aC.hour = 0
        aC.minute = 0
        
        self.hourOfAlarm.EditLabel(aC.hour, aC.minute)
        self.page.tkraise()
        self.menuFrame.tkraise()        
        
    def AddAlarm(self):  
    
        alarm = Alarms(True, aC.hour, aC.minute, 3, False, "opis", aC.color)
        
        self.menuFrame.tkraise()
        self.page.tkraise()
        self.listOfAlarms.ShowAlarms()                
        
        
    def AddOrSubtract(self, time, number):
        
        if time == "hour":
            
            if aC.hour + number >= 0 and aC.hour + number <= 23:
                
                aC.hour += number

            elif aC.hour + number < 0:
                
                aC.hour = 23
                
            elif aC.hour + number > 23:
                
                aC.hour = 0            
            
        elif time == "minute":
            
            if aC.minute + number >= 0 and aC.minute + number <= 59:
                
                aC.minute += number
                
            elif aC.minute + number < 0:
                
                aC.minute = 59
                
            elif aC.minute + number > 59:
                
                aC.minute = 0                     
            
        self.hourOfAlarm.EditLabel(aC.hour, aC.minute)
            
        
        