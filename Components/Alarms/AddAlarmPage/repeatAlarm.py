from xml.etree.ElementTree import TreeBuilder
import Components.Alarms.AddAlarmPage.alarmConfiguration as aC
from PIL import Image, ImageTk
from tkinter import CENTER, Button, SUNKEN
from functools import partial

class RepeatAlarm:
    
    frame = None
    btnMonday = None
    btnTuesday = None
    btnWednesday = None
    btnThursday = None
    btnFriday = None
    btnSaturday = None
    btnSunday = None
    circle = None
    blueCircle = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.circle = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\circle.png").resize((35, 35)))
        self.blueCircle = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\blue-circle.png").resize((35, 35)))
        self.CreateButtonsOfDays()
        
    def CreateButtonsOfDays(self):
        
        self.btnMonday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, text = "Mon", command= partial(self.SetDay, "monday"), compound=CENTER, font=("Calibri", 10))
        self.btnMonday.place(x = 10, y = 225, width=37, height=37)
        
        self.btnTuesday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, text = "Tue", command= partial(self.SetDay, "tuesday"), compound=CENTER, font=("Calibri", 10))
        self.btnTuesday.place(x = 50, y = 225, width=37, height=37)
        
        self.btnWednesday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, text = "Wed", command= partial(self.SetDay, "wednesday"), compound=CENTER, font=("Calibri", 10))
        self.btnWednesday.place(x = 90, y = 225, width=37, height=37)
        
        self.btnThursday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, text = "Thu", command= partial(self.SetDay, "thursday"), compound=CENTER, font=("Calibri", 10))
        self.btnThursday.place(x = 130, y = 225, height=37, width=37)
        
        self.btnFriday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, text = "Fri", command= partial(self.SetDay, "friday"), compound=CENTER, font=("Calibri", 10))
        self.btnFriday.place(x = 170, y = 225, width=37, height=37)
        
        self.btnSaturday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, text = "Sat", command= partial(self.SetDay, "saturday"), compound=CENTER, font=("Calibri", 10))
        self.btnSaturday.place(x = 210, y = 225, width=37, height=37)
        
        self.btnSunday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, text = "Sun", command= partial(self.SetDay, "sunday"), compound=CENTER, font=("Calibri", 10))
        self.btnSunday.place(x = 250, y = 225, width=37, height=37)
        
    def SetDay(self, day):
        
        if day == "monday":
        
            if aC.days["monday"] == False:
                
                aC.days["monday"] = True
                
            elif aC.days["monday"] == True:
                
                aC.days["monday"] = False
                
        elif day == "tuesday":
            
            if aC.days["tuesday"] == True:
                
                aC.days["tuesday"] = False
            
            elif aC.days["tuesday"] == False:
                
                aC.days["tuesday"] = True
                
        elif day == "wednesday":
            
            if aC.days["wednesday"] == True:
                
                aC.days["wednesday"] = False
            
            elif aC.days["wednesday"] == False:
                
                aC.days["wednesday"] = True
                
        elif day == "thursday":
            
            if aC.days["thursday"] == True:
                
                aC.days["thursday"] = False
            
            elif aC.days["thursday"] == False:
                
                aC.days["thursday"] = True
                
        elif day == "friday":
            
            if aC.days["friday"] == True:
                
                aC.days["friday"] = False
            
            elif aC.days["friday"] == False:
                
                aC.days["friday"] = True
                
        elif day == "saturday":
            
            if aC.days["saturday"] == True:
                
                aC.days["saturday"] = False
            
            elif aC.days["saturday"] == False:
                
                aC.days["saturday"] = True
                
        elif day == "sunday":
                
            if aC.days["sunday"] == True:
                
                aC.days["sunday"] = False
            
            elif aC.days["sunday"] == False:
                
                aC.days["sunday"] = True
                
        self.EditButtons()
            
        
    def EditButtons(self):
        
        if aC.days["monday"] == True:
            
            self.btnMonday.configure(image = self.blueCircle)
            
        elif aC.days["monday"] == False:
            
            self.btnMonday.configure(image = self.circle)
            
        if aC.days["tuesday"] == True:
            
            self.btnTuesday.configure(image = self.blueCircle)
            
        elif aC.days["tuesday"] == False:
            
            self.btnTuesday.configure(image = self.circle)
            
        if aC.days["wednesday"] == True:
            
            self.btnWednesday.configure(image = self.blueCircle)
            
        elif aC.days["wednesday"] == False:
            
            self.btnWednesday.configure(image = self.circle)
            
        if aC.days["thursday"] == True:
            
            self.btnThursday.configure(image = self.blueCircle)
            
        elif aC.days["thursday"] == False:
            
            self.btnThursday.configure(image = self.circle)
            
        if aC.days["friday"] == True:
            
            self.btnFriday.configure(image = self.blueCircle)
            
        elif aC.days["friday"] == False:
            
            self.btnFriday.configure(image = self.circle)
            
        if aC.days["saturday"] == True:
            
            self.btnSaturday.configure(image = self.blueCircle)
        
        elif aC.days["saturday"] == False:
            
            self.btnSaturday.configure(image = self.circle)
            
        if aC.days["sunday"] == True:
            
            self.btnSunday.configure(image = self.blueCircle)
            
        elif aC.days["sunday"] == False:
            
            self.btnSunday.configure(image = self.circle)
            
            
        

        
        