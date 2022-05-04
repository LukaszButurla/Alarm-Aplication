from tkinter import Label

class TimepieceTxt:
    
    timepieceTxt = None
    frame = None
    startHour = 00
    startMinute = 00
    startSecond = 00
    hourToEnd = None
    minuteToEnd = None
    secondToEnd = None
    start = False
    pause = False
    
    def __init__(self, frame):
        
        self.frame = frame
        self.ShowTimepiece()
        
    def ShowTimepiece(self):
        
        self.timepieceTxt = Label(self.frame, text = "23:59:59", bg = "white", font=("Calibri", 30))
        self.timepieceTxt.place(x = 50, y = 225, width=200, height=60)
        
    def EditTxt(self, hour, minute, second):
        
        self.timepieceTxt.configure(text = "{}:{}.{}".format(hour, minute, second))
        
    def StartTimepiece(self):
        
        self.start = True        
        
    def ResetTimepiece(self):
        
        self.start = False
        self.pause = False
        
    def PauseTimepiece(self):
        
        if self.pause == True:
            
            self.pause = False
        
        elif self.pause == False:
            
            self.pause = True
            
        
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