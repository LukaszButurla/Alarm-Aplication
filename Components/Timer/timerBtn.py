from tkinter import Button
from Components.Timer.timer import Timer
from PIL import Image, ImageTk
from Assets.Timer import *

class TimerButtons:

    frame = None
    btnStart = None
    btnStopStart = None
    BtnReset = None
    start = False
    pause = False
    timer = None
    startImg = None
    pauseImg = None
    resetImg = None

    def __init__(self, frame):

        self.startImg = ImageTk.PhotoImage(Image.open(r"Assets\Timer\play.png").resize((40, 40)))
        self.pauseImg = ImageTk.PhotoImage(Image.open(r"Assets\Timer\pause.png").resize((40, 40)))
        self.resetImg = ImageTk.PhotoImage(Image.open(r"Assets\Timer\stop-button.png").resize((40, 40)))
        
        self.frame = frame
        self.CreateButtons()
        self.PlaceButtons()
        self.timer = Timer(self.frame)

    def CreateButtons(self):

        self.btnStart = Button(self.frame, image=self.startImg, borderwidth=0, command = self.StartTimer, bg = "white")
        self.btnStopStart = Button(self.frame, borderwidth=0, text = "P", command = self.StopStart ,bg = "white")
        self.BtnReset = Button(self.frame, image=self.resetImg, borderwidth=0, text = "R", command = self.ResetTimer, bg = "white")
        
    def PlaceButtons(self):
        
        if self.start == False:
    
            self.btnStart.place(x = 135, y = 300, height=40, width=40)
            self.btnStopStart.place_forget()
            self.BtnReset.place_forget()

        elif self.start == True:

            self.btnStart.place_forget()
            self.btnStopStart.place(x = 180, y = 300, height=40, width=40)
            self.BtnReset.place(x = 100, y = 300, height=40, width=40)
            
        if self.pause == True:
            
            self.btnStopStart.configure(image = self.startImg)
            
        elif self.pause == False:
            
            self.btnStopStart.configure(image = self.pauseImg)

            
    def StartTimer(self):
    
        self.start = True
        self.PlaceButtons()
        self.timer.StartTimer(self.start)


    def StopStart(self):

        if self.pause == True:

            self.pause = False

        elif self.pause == False:

            self.pause = True

        self.timer.StartStop()
        self.PlaceButtons()

    def ResetTimer(self):

        self.start = False
        self.pause = False
        self.PlaceButtons()
        self.timer.ResetTime()
