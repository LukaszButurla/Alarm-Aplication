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
        
        self.btnMonday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, activebackground="white",text = "Mon", command= partial(self.SetDay, "monday"), compound=CENTER, font=("Calibri", 10), bg = "white")
        self.btnMonday.place(x = 10, y = 225, width=37, height=37)
        
        self.btnTuesday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, activebackground="white",text = "Tue", command= partial(self.SetDay, "tuesday"), compound=CENTER, font=("Calibri", 10), bg = "white")
        self.btnTuesday.place(x = 50, y = 225, width=37, height=37)
        
        self.btnWednesday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, activebackground="white",text = "Wed", command= partial(self.SetDay, "wednesday"), compound=CENTER, font=("Calibri", 10), bg = "white")
        self.btnWednesday.place(x = 90, y = 225, width=37, height=37)
        
        self.btnThursday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, activebackground="white",text = "Thu", command= partial(self.SetDay, "thursday"), compound=CENTER, font=("Calibri", 10), bg = "white")
        self.btnThursday.place(x = 130, y = 225, height=37, width=37)
        
        self.btnFriday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, activebackground="white",text = "Fri", command= partial(self.SetDay, "friday"), compound=CENTER, font=("Calibri", 10), bg = "white")
        self.btnFriday.place(x = 170, y = 225, width=37, height=37)
        
        self.btnSaturday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, activebackground="white",text = "Sat", command= partial(self.SetDay, "saturday"), compound=CENTER, font=("Calibri", 10), bg = "white")
        self.btnSaturday.place(x = 210, y = 225, width=37, height=37)
        
        self.btnSunday = Button(self.frame, relief=SUNKEN, image = self.circle, borderwidth=0, activebackground="white",text = "Sun", command= partial(self.SetDay, "sunday"), compound=CENTER, font=("Calibri", 10), bg = "white")
        self.btnSunday.place(x = 250, y = 225, width=37, height=37)
        
    def SetDay(self, day):
        
        if day == "monday":
        
            if 1 in aC.days:
                
                aC.days.remove(1)
                
            elif not 1 in aC.days:
                
                aC.days.append(1)
                
        elif day == "tuesday":
            
            if 2 in aC.days:
                
                aC.days.remove(2)
            
            elif not 2 in aC.days:
                
                aC.days.append(2)
                
        elif day == "wednesday":
            
            if 3 in aC.days:
                
                aC.days.remove(3)
            
            elif not 3 in aC.days:
                
                aC.days.append(3)
                
        elif day == "thursday":
            
            if 4 in aC.days:
                
                aC.days.remove(4)
            
            elif not 4 in aC.days:
                
                aC.days.append(4)
                
        elif day == "friday":
            
            if 5 in aC.days:
                
                aC.days.remove(5)
            
            elif not 5 in aC.days:
            
                aC.days.append(5)
                
        elif day == "saturday":
            
            if 6 in aC.days:
                
                aC.days.remove(6)
            
            elif not 6 in aC.days:
                
                aC.days.append(6)
                
        elif day == "sunday":
                
            if 7 in aC.days:
                
                aC.days.remove(7)
            
            elif not 7 in aC.days:
                
                aC.days.append(7)
                
        self.EditButtons()
            
        
    def EditButtons(self):
        
        if 1 in aC.days:
            
            self.btnMonday.configure(image = self.blueCircle)
            
        elif not 1 in aC.days:
            
            self.btnMonday.configure(image = self.circle)
            
        if 2 in aC.days:
            
            self.btnTuesday.configure(image = self.blueCircle)
            
        elif not 2 in aC.days:
            
            self.btnTuesday.configure(image = self.circle)
            
        if 3 in aC.days:
            
            self.btnWednesday.configure(image = self.blueCircle)
            
        elif not 3 in aC.days:
            
            self.btnWednesday.configure(image = self.circle)
            
        if 4 in aC.days:
            
            self.btnThursday.configure(image = self.blueCircle)
            
        elif not 4 in aC.days:
            
            self.btnThursday.configure(image = self.circle)
            
        if 5 in aC.days:
            
            self.btnFriday.configure(image = self.blueCircle)
            
        elif not 5 in aC.days:
            
            self.btnFriday.configure(image = self.circle)
            
        if 6 in aC.days:
            
            self.btnSaturday.configure(image = self.blueCircle)
        
        elif not 6 in aC.days:
            
            self.btnSaturday.configure(image = self.circle)
            
        if 7 in aC.days:
            
            self.btnSunday.configure(image = self.blueCircle)
            
        elif not 7 in aC.days:
            
            self.btnSunday.configure(image = self.circle)
            
            
        

        
        