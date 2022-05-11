from tkinter import SUNKEN, Button
import Components.Alarms.AddAlarmPage.alarmConfiguration as aC
from Components.Alarms.AddAlarmPage.hourOfAlarm import HourOfAlarm
from PIL import Image, ImageTk
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
    addImg = None
    subtractImg = None
    
    def __init__(self, frame, page, menuFrame, list):
        
        self.subtractImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\subtracting-button.png").resize((20, 20)))
        self.addImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\add.png").resize((20, 20)))
        
        self.page = page
        self.menuFrame = menuFrame
        self.listOfAlarms = list
        self.frame = frame
        self.hourOfAlarm = HourOfAlarm(self.frame)
        self.CreateButtonsHour()
        
    def CreateButtonsHour(self):
        
        self.addHourBtn = Button(self.frame, image = self.addImg, borderwidth=0, relief=SUNKEN, bg = "white", activebackground="white",  command=partial(self.AddOrSubtract, "hour", 1))
        self.addHourBtn.place(x = 110, y = 60)
        
        self.subtractHourBtn = Button(self.frame, image = self.subtractImg, borderwidth=0, relief=SUNKEN, bg = "white", activebackground="white",command=partial(self.AddOrSubtract, "hour", -1))
        self.subtractHourBtn.place(x = 110, y = 150)
        
        self.addMinuteBtn = Button(self.frame, image = self.addImg, borderwidth=0, relief=SUNKEN, bg = "white", activebackground="white",command=partial(self.AddOrSubtract, "minute", 1))
        self.addMinuteBtn.place(x = 200, y = 60)
        
        self.subtractMinuteBtn = Button(self.frame, image = self.subtractImg, borderwidth=0, relief=SUNKEN, bg = "white", activebackground="white",command=partial(self.AddOrSubtract, "minute", -1))
        self.subtractMinuteBtn.place(x = 200, y = 150)
        
        
    def CreateButtonsAddCancel(self):
        
        self.cancelBtn = Button(self.frame, text = "Cancel", command = self.Cancel)
        self.cancelBtn.place(x = 20, y = 500)
        
        self.addAlarmBtn = Button(self.frame, text = "Add", command = self.AddAlarm)
        self.addAlarmBtn.place(x = 230, y = 500)  
        
    def CreateButtonsEditCancel(self):
        
        self.cancelBtn = Button(self.frame, text = "Cancel", command = self.Cancel)
        self.cancelBtn.place(x = 20, y = 500)
        
        self.addAlarmBtn = Button(self.frame, text = "Edit", command = self.EditAlarm)
        self.addAlarmBtn.place(x = 230, y = 500)               
        
    def EditAlarm(self):
                
        aC.alarm.hour = aC.hour
        aC.alarm.minute = aC.minute
        aC.alarm.color = aC.color
        aC.alarm.days = aC.days
        
        self.menuFrame.tkraise()
        self.page.tkraise()
        self.listOfAlarms.ShowAlarms()
                    
    def Cancel(self):        
        
        self.page.tkraise()
        self.menuFrame.tkraise()        
        
    def AddAlarm(self):  
    
        alarm = Alarms(True, aC.hour, aC.minute, aC.days, False, "opis", aC.color, False)        
        
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
            
        
        