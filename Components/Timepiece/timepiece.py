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
    pauseStart = None
    pauseTime = 0
    
    def __init__(self, frame):
        
        self.frame = frame
        self.ShowTimepiece()
        
    def ShowTimepiece(self):
        
        self.timepieceTxt = Label(self.frame, text = "0:00:00", bg = "white", font=("Calibri", 45))
        self.timepieceTxt.place(x = 5, y = 225, width=300, height=80)
        
    def EditTxt(self, hour, minute, second):
        
        self.timepieceTxt.configure(text = "{}:{}.{}".format(hour, minute, second))
        
    def StartTimepiece(self):
        
        if int(self.startHour) > 0 or int(self.startMinute) > 0 or int(self.startSecond) > 0:
        
            self.hourToEnd = self.startHour
            self.minuteToEnd = self.startMinute
            self.secondToEnd = self.startSecond
            
            self.startTime = time()
            self.timeToEnd = int(self.hourToEnd) * 3600 + int(self.minuteToEnd) * 60 + int(self.secondToEnd)
            print(self.timeToEnd, "start")
            self.endTime = self.startTime + self.timeToEnd
            self.start = True  
            self.deltaStart = time()     
            
    def ResetTimepiece(self):
        
        self.start = False
        self.pause = False
        self.startMinute, self.startSecond = self.CheckNumberLen(self.startMinute, self.startSecond)
        self.EditTxt(self.startHour, self.startMinute, self.startSecond)
        
    def PauseTimepiece(self):
        
        if self.pause == True:
            
            self.pause = False
            self.pauseTime = time() - self.pauseStart
            self.timeToEnd += self.pauseTime
            
        
        elif self.pause == False:
            
            self.pause = True
            
            self.pauseStart = time()
            
    def Countdown(self):
        
        if self.start == True and self.pause == False and self.timeToEnd > 1:            
            
            delta = time() - self.deltaStart
            self.deltaStart = time()
            
            self.timeToEnd = self.timeToEnd - delta
            
            self.hourToEnd = floor(self.timeToEnd / 3600)
            self.minuteToEnd = floor((self.timeToEnd - self.hourToEnd * 3600) / 60)
            self.secondToEnd = self.timeToEnd - self.hourToEnd * 3600 - self.minuteToEnd * 60
            
            self.secondToEnd = str(self.secondToEnd)
            dot = self.secondToEnd.find(".")
            self.secondToEnd = self.secondToEnd[:dot]
            
            self.minuteToEnd, self.secondToEnd = self.CheckNumberLen(self.minuteToEnd, self.secondToEnd)          
            
            
            self.EditTxt(self.hourToEnd, self.minuteToEnd, self.secondToEnd)
            
        elif self.start == True and self.timeToEnd < 1:
            
            self.ResetTimepiece()
            
    def CheckNumberLen(self, minute, second):    
               
                    
        if len(str(minute)) < 2:
                
            minute = "0" + str(minute)
            
        else:
                
            minute = str(minute)
                
        if len(str(second)) < 2:
                
            second = "0" + str(second)[:1]
            
        return minute, second
            
            
        
    def AddOrSubtract(self, number, t):
    
        if t == "hour":

            if int(self.startHour) + number >= 0 and int(self.startHour) + number <= 23:
                
                self.startHour = int(self.startHour) + number                
                
                
            elif int(self.startHour) + number < 0:
                
                self.startHour = 23
         
            elif self.startHour + number > 23:
                
                self.startHour = 0               
        
        elif t == "minute":
            
            if int(self.startMinute) + number >= 0 and int(self.startMinute) + number <= 59:
                
                self.startMinute = int(self.startMinute) + number                         
                
            elif self.startMinute + number < 0:
                
                self.startMinute = 59
                
            elif self.startMinute + number > 59:
                
                self.startMinute = 0
                
            
        elif t == "second":
               
            if int(self.startSecond) + number >= 0 and int(self.startSecond) + number <= 59:
                
                self.startSecond = int(self.startSecond) + number
                
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