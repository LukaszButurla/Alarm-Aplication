from xml.etree.ElementTree import TreeBuilder
from Components.Alarms.AddAlarmPage.alarmConfiguration import Configuration
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
    configuration = None
    monday = None
    tuesday = None
    wednesday = None
    thursday = None
    friday = None
    saturday = None
    sunday = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.circle = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\circle.png").resize((35, 35)))
        self.blueCircle = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\blue-circle.png").resize((35, 35)))
        self.configuration = Configuration()
        self.monday = self.configuration.monday
        self.tuesday = self.configuration.tuesday
        self.wednesday = self.configuration.wednesday
        self.thursday = self.configuration.thursday
        self.friday = self.configuration.friday
        self.saturday = self.configuration.saturday
        self.sunday = self.configuration.sunday
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
        
            if self.monday == False:
                
                self.monday = True
                
            elif self.monday == True:
                
                self.monday = False
                
        elif day == "tuesday":
            
            if self.tuesday == True:
                
                self.tuesday = False
            
            elif self.tuesday == False:
                
                self.tuesday = True
                
        elif day == "wednesday":
            
            if self.wednesday == True:
                
                self.wednesday = False
            
            elif self.wednesday == False:
                
                self.wednesday = True
                
        elif day == "thursday":
            
            if self.thursday == True:
                
                self.thursday = False
            
            elif self.thursday == False:
                
                self.thursday = True
                
        elif day == "friday":
            
            if self.friday == True:
                
                self.friday = False
            
            elif self.friday == False:
                
                self.friday = True
                
        elif day == "saturday":
            
            if self.saturday == True:
                
                self.saturday = False
            
            elif self.saturday == False:
                
                self.saturday = True
                
        elif day == "sunday":
                
            if self.sunday == True:
                
                self.sunday = False
            
            elif self.sunday == False:
                
                self.sunday = True
                
        self.EditButtons()
            
        
    def EditButtons(self):
        
        if self.monday == True:
            
            self.btnMonday.configure(image = self.blueCircle)
            
        elif self.monday == False:
            
            self.btnMonday.configure(image = self.circle)
            
        if self.tuesday == True:
            
            self.btnTuesday.configure(image = self.blueCircle)
            
        elif self.tuesday == False:
            
            self.btnTuesday.configure(image = self.circle)
            
        if self.wednesday == True:
            
            self.btnWednesday.configure(image = self.blueCircle)
            
        elif self.wednesday == False:
            
            self.btnWednesday.configure(image = self.circle)
            
        if self.thursday == True:
            
            self.btnThursday.configure(image = self.blueCircle)
            
        elif self.thursday == False:
            
            self.btnThursday.configure(image = self.circle)
            
        if self.friday == True:
            
            self.btnFriday.configure(image = self.blueCircle)
            
        elif self.friday == False:
            
            self.btnFriday.configure(image = self.circle)
            
        if self.saturday == True:
            
            self.btnSaturday.configure(image = self.blueCircle)
        
        elif self.saturday == False:
            
            self.btnSaturday.configure(image = self.circle)
            
        if self.sunday == True:
            
            self.btnSunday.configure(image = self.blueCircle)
            
        elif self.sunday == False:
            
            self.btnSunday.configure(image = self.circle)
            
            
        

        
        