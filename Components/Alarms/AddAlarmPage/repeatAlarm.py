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
        
            if aC.monday == False:
                
                aC.monday = True
                
            elif aC.monday == True:
                
                aC.monday = False
                
        elif day == "tuesday":
            
            if aC.tuesday == True:
                
                aC.tuesday = False
            
            elif aC.tuesday == False:
                
                aC.tuesday = True
                
        elif day == "wednesday":
            
            if aC.wednesday == True:
                
                aC.wednesday = False
            
            elif aC.wednesday == False:
                
                aC.wednesday = True
                
        elif day == "thursday":
            
            if aC.thursday == True:
                
                aC.thursday = False
            
            elif aC.thursday == False:
                
                aC.thursday = True
                
        elif day == "friday":
            
            if aC.friday == True:
                
                aC.friday = False
            
            elif aC.friday == False:
                
                aC.friday = True
                
        elif day == "saturday":
            
            if aC.saturday == True:
                
                aC.saturday = False
            
            elif aC.saturday == False:
                
                aC.saturday = True
                
        elif day == "sunday":
                
            if aC.sunday == True:
                
                aC.sunday = False
            
            elif aC.sunday == False:
                
                aC.sunday = True
                
        self.EditButtons()
            
        
    def EditButtons(self):
        
        if aC.monday == True:
            
            self.btnMonday.configure(image = self.blueCircle)
            
        elif aC.monday == False:
            
            self.btnMonday.configure(image = self.circle)
            
        if aC.tuesday == True:
            
            self.btnTuesday.configure(image = self.blueCircle)
            
        elif aC.tuesday == False:
            
            self.btnTuesday.configure(image = self.circle)
            
        if aC.wednesday == True:
            
            self.btnWednesday.configure(image = self.blueCircle)
            
        elif aC.wednesday == False:
            
            self.btnWednesday.configure(image = self.circle)
            
        if aC.thursday == True:
            
            self.btnThursday.configure(image = self.blueCircle)
            
        elif aC.thursday == False:
            
            self.btnThursday.configure(image = self.circle)
            
        if aC.friday == True:
            
            self.btnFriday.configure(image = self.blueCircle)
            
        elif aC.friday == False:
            
            self.btnFriday.configure(image = self.circle)
            
        if aC.saturday == True:
            
            self.btnSaturday.configure(image = self.blueCircle)
        
        elif aC.saturday == False:
            
            self.btnSaturday.configure(image = self.circle)
            
        if aC.sunday == True:
            
            self.btnSunday.configure(image = self.blueCircle)
            
        elif aC.sunday == False:
            
            self.btnSunday.configure(image = self.circle)
            
            
        

        
        