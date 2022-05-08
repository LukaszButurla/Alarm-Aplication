from Components.Alarms.AddAlarmPage.colorOfAlarm import ColorOfAlarm
from Components.Alarms.AddAlarmPage.repeatAlarm import RepeatAlarm
from Components.Alarms.AddAlarmPage.colorOfAlarm import ColorOfAlarm
from Components.Alarms.AddAlarmPage.buttons import Buttons
import Components.Alarms.AddAlarmPage.alarmConfiguration as aC
from tkinter import Frame

class EditPage:
    
    window = None
    editFrame = None
    menuFrame = None
    page = None
    buttons = None
    listOfAlarms = None
    repeatAlarm = None
    colorOfAlarm = None

    def __init__(self, window, menuFrame, page, list):
        
        self.frame = window
        self.menuFarme = menuFrame
        self.page = page
        self.listOfAlarms = list
        self.CreateFrame()
        self.repeatAlarm = RepeatAlarm(self.editFrame)
        self.colorOfAlarm = ColorOfAlarm(self.editFrame)
        self.buttons = Buttons(self.editFrame, self.page, menuFrame, self.listOfAlarms)
        self.buttons.CreateButtonsEditCancel()
        
    def CreateFrame(self):
        
        self.editFrame = Frame(self.window, width=350, height=550)
        
    def ShowEditFrame(self, alarm):
        
        aC.hour = alarm.hour
        aC.minute = alarm.minute
        aC.color = alarm.color
        aC.days = alarm.days
        aC.alarm = alarm
        
        self.buttons.hourOfAlarm.EditLabel(aC.hour, aC.minute)
        self.colorOfAlarm.EditButtons()
        self.repeatAlarm.EditButtons()
        
        self.editFrame.place(x = 0, y = 0)
        self.editFrame.tkraise()   
            