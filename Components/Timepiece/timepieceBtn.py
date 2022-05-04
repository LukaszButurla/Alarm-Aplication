from tkinter import Button
from functools import partial
from Components.Timepiece.timepiece import TimepieceTxt

class TimepieceButtons:
    
    frame = None
    timepiece = None
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
    startHour = 00
    startMinute = 00
    startSecond = 00
    
    def __init__(self, frame):
        
        self.frame = frame
        self.timepiece = TimepieceTxt(self.frame)
        self.CreateButtons()
        self.PlaceButtons()
        self.timepiece.EditTxt("0", "00", "00")
        
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
        self.timepiece.EditTxt(self.startHour, self.startSecond, self.startSecond)
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

            if self.startHour + number >= 0 and self.startHour + number <= 23:
                
                self.startHour += number
                
                
                
            elif self.startHour + number < 0:
                
                self.startHour = 23
         
            elif self.startHour + number > 23:
                
                self.startHour = 0               
        
        elif t == "minute":
            
            if self.startMinute + number >= 0 and self.startMinute + number <= 59:
                
                self.startMinute += number                
                
                
            elif self.startMinute + number < 0:
                
                self.startMinute = 59
                
            elif self.startMinute + number > 59:
                
                self.startMinute = 0
                
            
        elif t == "second":
               
            if self.startSecond + number >= 0 and self.startSecond + number <= 59:
                
                self.startSecond += number
                
            elif self.startSecond + number < 0:
                
                self.startSecond = 59
                
            elif self.startSecond + number > 59:
                
                self.startSecond = 0
                
        if len(str(self.startMinute)) < 2:
                    
            strMinute = "0" + str(self.startMinute)
                    
        else:
                    
            strMinute = str(self.startMinute)         
            
        if len(str(self.startSecond)) < 2:
            
            strSecond = "0" + str(self.startSecond)
            
        else:
            
            strSecond = str(self.startSecond)
                
        strHour = str(self.startHour)
        
        self.timepiece.EditTxt(strHour, strMinute, strSecond)
        
                
