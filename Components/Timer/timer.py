from datetime import datetime
from tkinter import Label
from math import floor
import time

class Timer:
    
    frame = None
    timeStart = None
    timerTxt = None
    start = False
    pause = False
    timeStart = None
    timer = 0
    pauseTime = 0
    pauseStart = None
    pauseStop = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.ShowTimer()
        
    def ShowTimer(self):
        
        self.timerTxt = Label(self.frame, text = "0:00:00.00", font=("Calibri", 30), bg = "white")
        self.timerTxt.place(x = 50, y = 225, width=200, height=60)
        
    def EditTimerTxt(self, hour, minute, seconds, miliseconds):
        
        self.timerTxt.configure(text = "{}:{}:{}.{}".format(hour, minute, seconds, miliseconds))
        
    def ResetTime(self):
        
        self.start = False
        self.pause = False
        self.timer = 0
        self.pauseTime = 0
        self.EditTimerTxt("0","00","00","00")
        
    def StartTimer(self, start):
        
        self.start = start
        self.timeStart = time.time()
        
    def StartStop(self):
               
        if self.pause == True:
            
            self.pause = False
            
            self.pauseTime += (time.time() - self.pauseStart)
            print(self.pauseTime)
            
        elif self.pause == False:
            
            self.pause = True
            self.pauseStart = time.time()
        
    def Count(self):
        
        if self.start == True and self.pause == False:            
            
            self.timer = time.time() - (self.timeStart + self.pauseTime)
            
            hour = self.timer / 3600
            hour = floor(hour)
            self.timer -= hour * 3600
            
            minute = self.timer / 60
            minute = floor(minute)
            self.timer -= minute * 60
            
            if len(str(minute)) < 2:
                
                minute = "0" + str(minute)            
            
            dot = str(self.timer).find(".")
            
            second = str(self.timer)[:dot]
            
            if len(second) < 2:
                
                second = "0" + second
            
            milisecond = str(self.timer)[2:4]
            
            
            self.EditTimerTxt(hour, minute, second, milisecond)
            
            
        
        
        
            
        