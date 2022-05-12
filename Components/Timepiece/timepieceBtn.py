from tkinter import Button
from functools import partial
from Components.Timepiece.timepiece import TimepieceTxt
from PIL import ImageTk, Image
from Assets.Timepiece import *

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
    addImg = None
    subtractImg = None
    startImg = None
    resetImg = None
    pauseImg = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.timepiece = TimepieceTxt(self.frame)
        
        self.addImg = ImageTk.PhotoImage(Image.open(r"Assets\Timepiece\add.png").resize((30, 30)))
        self.subtractImg = ImageTk.PhotoImage(Image.open(r"Assets\Timepiece\subtracting-button.png").resize((30, 30)))
        self.startImg = ImageTk.PhotoImage(Image.open(r"Assets\Timepiece\play.png").resize((50, 50)))
        self.pauseImg = ImageTk.PhotoImage(Image.open(r"Assets\Timepiece\pause.png").resize((50, 50)))
        self.resetImg = ImageTk.PhotoImage(Image.open(r"Assets\Timepiece\stop-button.png").resize((50, 50)))
        
        self.CreateButtons()
        self.PlaceButtons(self.timepiece.start, self.timepiece.pause)
        self.timepiece.EditTxt("0", "00", "00")
        
    def CreateButtons(self):
        
        self.addHourBtn = Button(self.frame, image=self.addImg, borderwidth=0, bg = "white", command=partial(self.timepiece.AddOrSubtract, 1, "hour"))
        self.addMinuteBtn = Button(self.frame, image=self.addImg, borderwidth=0, bg = "white", command = partial(self.timepiece.AddOrSubtract, 1, "minute"))
        self.addSecondBtn = Button(self.frame, image=self.addImg, borderwidth=0, bg = "white", command = partial(self.timepiece.AddOrSubtract, 1, "second"))
        self.subtractHourBtn = Button(self.frame, image = self.subtractImg, borderwidth=0, bg = "white", command=partial(self.timepiece.AddOrSubtract, -1, "hour"))
        self.subtractMinuteBtn = Button(self.frame, image = self.subtractImg, borderwidth=0, bg = "white", command=partial(self.timepiece.AddOrSubtract, -1, "minute"))
        self.subtractSecondBtn = Button(self.frame, image = self.subtractImg, borderwidth=0, bg = "white", command=partial(self.timepiece.AddOrSubtract, -1, "second"))
        
        self.startBtn = Button(self.frame, image=self.startImg, borderwidth=0, bg = "white", command=self.StartTimepiece)
        self.resetBtn = Button(self.frame, image=self.resetImg, borderwidth=0, bg = "white", command=self.ResetTimepiece)
        self.pauseBtn = Button(self.frame, borderwidth=0, bg = "white", command = self.PauseTimepiece)
        
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
            
        if start == False:
            
            self.addHourBtn.place(x = 60, y = 200)
            self.addMinuteBtn.place(x = 125, y = 200)
            self.addSecondBtn.place(x =200, y = 200)
            self.subtractHourBtn.place(x = 60, y = 305)
            self.subtractMinuteBtn.place(x = 125, y = 305)
            self.subtractSecondBtn.place(x = 200, y = 305)            
            self.startBtn.place( x = 125, y = 380)
            
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
            
            self.resetBtn.place(x = 80, y = 380)
            self.pauseBtn.place(x = 180, y= 380)
            
        if pause == True:
            
            self.pauseBtn.configure(image = self.startImg)
            
        elif pause == False:
            
            self.pauseBtn.configure(image=self.pauseImg)
            
            
    
        
                
