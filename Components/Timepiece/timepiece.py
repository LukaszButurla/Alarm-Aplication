from math import floor
from sqlite3 import Time
from tkinter import Label
from time import time

class TimepieceTxt:
    
    timepieceTxt = None
    frame = None
    startHour = 00
    startMinute = 00
    startSecond = 00
    hourToEnd = None
    minuteToEnd = None
    secondToEnd = None
    timeToEnd = None
    startTime = None
    endTime = None
    deltaStart = None
    start = False
    pause = False
    
    def __init__(self, frame):
        
        self.frame = frame
        self.ShowTimepiece()
        
    def ShowTimepiece(self):
        
        self.timepieceTxt = Label(self.frame, text = "0:00:00", bg = "white", font=("Calibri", 30))
        self.timepieceTxt.place(x = 50, y = 225, width=200, height=60)
        
    def EditTxt(self, hour, minute, second):
        
        self.timepieceTxt.configure(text = "{}:{}.{}".format(hour, minute, second))
        
    def StartTimepiece(self):
        
        self.hourToEnd = self.startHour
        self.minuteToEnd = self.startMinute
        self.secondToEnd = self.startSecond
        
        self.startTime = time()
        self.timeToEnd = self.hourToEnd * 3600 + self.minuteToEnd * 60 + self.secondToEnd
        print(self.timeToEnd, "start")
        self.endTime = self.startTime + self.timeToEnd
        self.start = True  
        self.deltaStart = time()     
        
    def ResetTimepiece(self):
        
        self.start = False
        self.pause = False
        self.CheckNumberLen()
        self.EditTxt(self.startHour, self.startMinute, self.startSecond)
        
    def PauseTimepiece(self):
        
        if self.pause == True:
            
            self.pause = False
        
        elif self.pause == False:
            
            self.pause = True
            
    def Countdown(self):
        
        if self.start == True and self.timeToEnd > 1:            
            
            delta = time() - self.deltaStart
            self.deltaStart = time()
            
            self.timeToEnd = self.timeToEnd - delta
            
            
            
            self.CheckNumberLen()          
            
            
            self.EditTxt(self.hourToEnd, self.minuteToEnd, self.secondToEnd)
            
        elif self.start == True and self.timeToEnd < 1:
            
            print("end")
            self.ResetTimepiece()
            
    def CheckNumberLen(self):    
        
        self.hourToEnd = floor(self.timeToEnd / 3600)
        self.minuteToEnd = floor((self.timeToEnd - self.hourToEnd * 3600) / 60)
        self.secondToEnd = self.timeToEnd - self.hourToEnd * 3600 - self.minuteToEnd * 60
            
        self.secondToEnd = str(self.secondToEnd)
        dot = self.secondToEnd.find(".")
        self.secondToEnd = self.secondToEnd[:dot]
            
        self.hourToEnd = floor(self.timeToEnd / 3600)
        
        if len(str(self.minuteToEnd)) < 2:
                
            self.minuteToEnd = "0" + str(self.minuteToEnd)
            
        else:
                
            self.minuteToEnd = str(self.minuteToEnd)
                
        if len(str(self.secondToEnd)) < 2:
                
            self.secondToEnd = "0" + str(self.secondToEnd)[:1]
            
            
        
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
        
        self.EditTxt(strHour, strMinute, strSecond)