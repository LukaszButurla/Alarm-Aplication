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
    
    def __init__(self, frame):
        
        self.frame = frame
        self.timepiece = TimepieceTxt(self.frame)
        self.CreateButtons()
        self.PlaceButtons(self.timepiece.start, self.timepiece.pause)
        self.timepiece.EditTxt("0", "00", "00")
        
    def CreateButtons(self):
        
        self.addHourBtn = Button(self.frame, text = "+", bg = "white", command=partial(self.timepiece.AddOrSubtract, 1, "hour"))
        self.addMinuteBtn = Button(self.frame, text = "+", bg = "white", command = partial(self.timepiece.AddOrSubtract, 1, "minute"))
        self.addSecondBtn = Button(self.frame, text = "+", bg = "white", command = partial(self.timepiece.AddOrSubtract, 1, "second"))
        self.subtractHourBtn = Button(self.frame, text = "-", bg = "white", command=partial(self.timepiece.AddOrSubtract, -1, "hour"))
        self.subtractMinuteBtn = Button(self.frame, text = "-", bg = "white", command=partial(self.timepiece.AddOrSubtract, -1, "minute"))
        self.subtractSecondBtn = Button(self.frame, text = "-", bg = "white", command=partial(self.timepiece.AddOrSubtract, -1, "second"))
        
        self.startBtn = Button(self.frame, text = ">", bg = "white", command=self.StartTimepiece)
        self.resetBtn = Button(self.frame, text = "R", bg = "white", command=self.ResetTimepiece)
        self.pauseBtn = Button(self.frame, text = "NP", bg = "white", command = self.PauseTimepiece)
        
    def StartTimepiece(self):
        
        self.timepiece.StartTimepiece()
        self.PlaceButtons(self.timepiece.start, self.timepiece.pause)
        
    def ResetTimepiece(self):
        
        self.timepiece.ResetTimepiece()
        self.PlaceButtons(self.timepiece.start, self.timepiece.pause)
        
    def PauseTimepiece(self):
        
        self.timepiece.PauseTimepiece()            
        self.PlaceButtons(self.timepiece.start, self.timepiece.pause)
            

        
        
    def PlaceButtons(self, start, pause):
        
        print(start)
        print(pause)
        
        if start == False:
            
            self.addHourBtn.place(x = 95, y = 200)
            self.addMinuteBtn.place(x = 140, y = 200)
            self.addSecondBtn.place(x = 185, y = 200)
            self.subtractHourBtn.place(x = 95, y = 280)
            self.subtractMinuteBtn.place(x = 140, y = 280)
            self.subtractSecondBtn.place(x = 185, y = 280)            
            self.startBtn.place( x = 140, y = 320)
            
            self.resetBtn.place_forget()
            self.pauseBtn.place_forget()
            
        elif start == True:
            
            self.startBtn.place_forget()
            self.addHourBtn.place_forget()
            self.addMinuteBtn.place_forget()
            self.addSecondBtn.place_forget()
            self.subtractHourBtn.place_forget()
            self.subtractMinuteBtn.place_forget()
            self.subtractSecondBtn.place_forget()
            
            self.resetBtn.place(x = 120, y = 320)
            self.pauseBtn.place(x = 160, y= 320)
            
        if pause == True:
            
            self.pauseBtn.configure(text = "P")
            
        elif pause == False:
            
            self.pauseBtn.configure(text = "NP")
            
            
    
        
                
