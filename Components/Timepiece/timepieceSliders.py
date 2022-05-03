from tkinter import Scale

class TimepieceSliders:
    
    frame = None
    sliderH = None
    sliderM = None
    sliderS = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.CreateSliders()
        
    def CreateSliders(self):
        
        self.sliderH = Scale(self.frame, from_=0, to=23)
        self.sliderH.place(x = 50, y = 150)
        
        self.sliderM = Scale(self.frame, from_=0, to=59)
        self.sliderM.place(x = 100, y = 150)
        
        self.sliderS = Scale(self.frame, from_=0, to=59)
        self.sliderS.place(x = 150, y = 150)
        