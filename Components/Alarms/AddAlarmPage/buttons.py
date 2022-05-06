from tkinter import Button
from Components.Alarms.AddAlarmPage.alarmConfiguration import Configuration
from Components.Alarms.AddAlarmPage.hourOfAlarm import HourOfAlarm
from functools import partial


class Buttons:
    
    frame = None
    hourOfAlarm = None
    alarmConfiguration = None
    addHourBtn = None
    subtractHourBtn = None
    addMinuteBtn = None
    subtractMinuteBtn = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.hourOfAlarm = HourOfAlarm(self.frame)
        self.alarmConfiguration = Configuration
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
        
    def AddOrSubtract(self, time, number):
        
        if time == "hour":
            
            self.alarmConfiguration.hour += number
            
        elif time == "minute":
            
            self.alarmConfiguration.minute += number
            
        self.hourOfAlarm.EditLabel(self.alarmConfiguration.hour, self.alarmConfiguration.minute)
            
        
        