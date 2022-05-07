
from tkinter import Button


class RepeatAlarm:
    
    frame = None
    btnMonday = None
    btnTuesday = None
    btnWednesday = None
    btnThursday = None
    btnFriday = None
    btnSaturday = None
    btnSunday = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.CreateButtonsOfDays()
        
    def CreateButtonsOfDays(self):
        
        self.btnMonday = Button(self.frame, text = "Mon")
        self.btnMonday.place(x = 40, y = 225, width=30, height=30)
        
        self.btnTuesday = Button(self.frame, text = "Tue")
        self.btnTuesday.place(x = 75, y = 225, width=30, height=30)
        
        self.btnWednesday = Button(self.frame, text = "Wed")
        self.btnWednesday.place(x = 110, y = 225, width=30, height=30)
        
        self.btnThursday = Button(self.frame, text = "Thu")
        self.btnThursday.place(x = 145, y = 225, height=30, width=30)
        
        self.btnFriday = Button(self.frame, text = "Fri")
        self.btnFriday.place(x = 180, y = 225, width=30, height=30)
        
        self.btnSaturday = Button(self.frame, text = "Sat")
        self.btnSaturday.place(x = 215, y = 225, width=30, height=30)
        
        self.btnSunday = Button(self.frame, text = "Sun")
        self.btnSunday.place(x = 250, y = 225, width=30, height=30)
        
        