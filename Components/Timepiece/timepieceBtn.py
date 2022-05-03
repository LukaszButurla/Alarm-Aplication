from tkinter import Button
from functools import partial
from Components.Timepiece.timepieceTxt import TimepieceTxt

class TimepieceButtons:
    
    frame = None
    timepieceTxt = None
    addHourBtn = None
    addMinuteBtn = None
    addSecondBtn = None
    subtractHourBtn = None
    subtractMinuteBtn = None
    subtractSecondBtn = None
    startBtn = None
    pauseBtn = None
    resetBtn = None
    start = False
    pause = False
    hour = 12
    minute = 30
    second = 30
    
    def __init__(self, frame):
        
        self.frame = frame
        self.timepieceTxt = TimepieceTxt(self.frame)
        self.CreateButtons()
        self.PlaceButtons()
        self.timepieceTxt.EditTxt(self.hour, self.minute, self.second)
        
    def CreateButtons(self):
        
        self.addHourBtn = Button(self.frame, text = "+", bg = "white", command=partial(self.AddOrSubtract, 1, "hour"))
        self.addMinuteBtn = Button(self.frame, text = "+", bg = "white", command = partial(self.AddOrSubtract, 1, "minute"))
        self.addSecondBtn = Button(self.frame, text = "+", bg = "white", command = partial(self.AddOrSubtract, 1, "second"))
        self.subtractHourBtn = Button(self.frame, text = "-", bg = "white", command=partial(self.AddOrSubtract, -1, "hour"))
        self.subtractMinuteBtn = Button(self.frame, text = "-", bg = "white", command=partial(self.AddOrSubtract, -1, "minute"))
        self.subtractSecondBtn = Button(self.frame, text = "-", bg = "white", command=partial(self.AddOrSubtract, -1, "second"))
        
        self.startBtn = Button(self.frame, text = ">", bg = "white", command=self.StartTimepiece)
        self.resetBtn = Button(self.frame, text = "R", bg = "white", command=self.ResetTimepiece)
        self.pauseBtn = Button(self.frame, text = "NP", bg = "white", command = self.PauseTimepiece)
        
    def StartTimepiece(self):
        
        self.start = True
        self.PlaceButtons()
        
    def ResetTimepiece(self):
        
        self.start = False
        self.PlaceButtons()
        
    def PauseTimepiece(self):
        
        if self.pause == True:
            
            self.pause = False
            self.pauseBtn.configure(text = "NP")
        
        elif self.pause == False:
            
            self.pause = True
            self.pauseBtn.configure(text = "P")
            
        self.PlaceButtons()
        
        
    def PlaceButtons(self):
        
        if self.start == False:
            
            self.addHourBtn.place(x = 95, y = 200)
            self.addMinuteBtn.place(x = 140, y = 200)
            self.addSecondBtn.place(x = 185, y = 200)
            self.subtractHourBtn.place(x = 95, y = 280)
            self.subtractMinuteBtn.place(x = 140, y = 280)
            self.subtractSecondBtn.place(x = 185, y = 280)            
            self.startBtn.place( x = 140, y = 320)
            
            self.resetBtn.place_forget()
            self.pauseBtn.place_forget()
            
        elif self.start == True:
            
            self.startBtn.place_forget()
            self.addHourBtn.place_forget()
            self.addMinuteBtn.place_forget()
            self.addSecondBtn.place_forget()
            self.subtractHourBtn.place_forget()
            self.subtractMinuteBtn.place_forget()
            self.subtractSecondBtn.place_forget()
            
            self.resetBtn.place(x = 120, y = 320)
            self.pauseBtn.place(x = 160, y= 320)
            
            
    def AddOrSubtract(self, number, t):

        if t == "hour":

            if self.hour + number >= 0 and self.hour + number <= 23:
                
                self.hour += number
                
            elif self.hour + number < 0:
                
                self.hour = 23
         
            elif self.hour + number > 23:
                
                self.hour = 0                
        
        elif t == "minute":
            
            if self.minute + number >= 0 and self.minute + number <= 59:
                
                self.minute += number
                
            elif self.minute + number < 0:
                
                self.minute = 59
                
            elif self.minute + number > 59:
                
                self.minute = 0
                
            
        elif t == "second":
               
            if self.second + number >= 0 and self.second + number <= 59:
                
                self.second += number
                
            elif self.second + number < 0:
                
                self.second = 59
                
            elif self.second + number > 59:
                
                self.second = 0
                
        self.timepieceTxt.EditTxt(self.hour, self.minute, self.second)
                
