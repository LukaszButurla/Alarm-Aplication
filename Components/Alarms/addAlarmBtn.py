from Components.Alarms.AddAlarmPage.addAlarmPage import AddAlarmPage
import Components.Alarms.AddAlarmPage.alarmConfiguration as aC
from PIL import Image, ImageTk
from tkinter import Button
from Assets.Alarms import *


class AddAlarmBtn:
    
    window = None
    frame = None
    menuFrame = None
    addBtn = None
    addImg = None
    addAlarmPage = None
    listOfAlarms = None
    
    def __init__(self, frame, menuFrame, window, list):
        
        self.listOfAlarms = list
        self.window = window
        self.frame = frame
        self.menuFrame = menuFrame
        self.addImg = ImageTk.PhotoImage(Image.open(r"Assets\Alarms\plus.png").resize((20, 20)))
        self.addAlarmPage = AddAlarmPage(self.window, self.frame, self.menuFrame, self.listOfAlarms)
        self.CreateAddBtn()
        
        
    def CreateAddBtn(self):
        
        self.addBtn = Button(self.frame, image = self.addImg, borderwidth= 0, bg = "white", command= self.OpenAddPage)
        self.addBtn.place(x = 250, y = 20)
        
    def OpenAddPage(self):        
        
        self.addAlarmPage.ShowAddFrame()
        self.ResetValues()
        
    def ResetValues(self):       
            
        aC.hour = 0
        aC.minute = 0
        aC.color = "white"
        aC.days = []
        
        self.addAlarmPage.colorOfAlarm.EditButtons()
        self.addAlarmPage.repeatAlarm.EditButtons()
        self.addAlarmPage.buttons.hourOfAlarm.EditLabel(aC.hour, aC.minute)
        
       