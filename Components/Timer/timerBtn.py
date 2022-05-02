from tkinter import Button

class TimerButtons:

    frame = None
    btnStart = None
    btnStopStart = None
    BtnReset = None
    start = False
    pause = False

    def __init__(self, frame):

        self.frame = frame
        self.CreateButtons()
        self.PlaceButtons()

    def CreateButtons(self):

        self.btnStart = Button(self.frame, text = "<", command = self.StartTimer)
        self.btnStopStart = Button(self.frame, text = "P", command = self.StopStopTimer)
        self.BtnReset = Button(self.frame, text = "R", command = self.ResetTimer)
        
    def PlaceButtons(self):
        
        if self.start == False:
    
            self.btnStart.place(x = 180, y = 300, height=30, width=30)
            self.btnStopStart.place_forget()

        elif self.start == True:

            self.btnStart.place_forget()
            self.btnStopStart.place(x = 140, y = 300, height=30, width=30)

        if self.pause == True:

            self.BtnReset.place(x = 100, y = 300, height=30, width=30)

        elif self.pause == False:

            self.BtnReset.place_forget()
            
    def StartTimer(self):
    
        self.start = True
        self.PlaceButtons()
        self.timer.StartStop(self.start)
        print("start")


    def StopStopTimer(self):

        if self.pause == True:

            self.pause = False

        elif self.pause == False:

            self.pause = True

        self.PlaceButtons()

    def ResetTimer(self):

        self.start = False
        self.pause = False
        self.PlaceButtons()
