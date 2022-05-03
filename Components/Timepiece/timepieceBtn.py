from tkinter import Button

class TimepieceButtons:
    
    frame = None
    addHourBtn = None
    addMinuteBtn = None
    addSecondBtn = None
    subtractHourBtn = None
    subtractMinuteBtn = None
    subtractSecondBtn = None
    start = False
    
    def __init__(self, frame):
        
        self.frame = frame
        self.CreateButtons()
        self.PlaceButtons()
        
    def CreateButtons(self):
        
        self.addHourBtn = Button(self.frame, text = "+", bg = "white")
        self.addMinuteBtn = Button(self.frame, text = "+", bg = "white")
        self.addSecondBtn = Button(self.frame, text = "+", bg = "white")
        self.subtractHourBtn = Button(self.frame, text = "-", bg = "white")
        self.subtractMinuteBtn = Button(self.frame, text = "-", bg = "white")
        self.subtractSecondBtn = Button(self.frame, text = "-", bg = "white")
        
    def PlaceButtons(self):
        
        if self.start == False:
            
            self.addHourBtn.place(x = 95, y = 200)
            self.addMinuteBtn.place(x = 140, y = 200)
            self.addSecondBtn.place(x = 185, y = 200)
            self.subtractHourBtn.place(x = 95, y = 280)
            self.subtractMinuteBtn.place(x = 140, y = 280)
            self.subtractSecondBtn.place(x = 185, y = 280)