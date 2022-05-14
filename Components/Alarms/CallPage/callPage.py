from tkinter import Label, Button, Frame

class CallPage:
    
    frame = None
    callFrame = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.CreateFrame()
        
    def CreateFrame(self):
        
        self.callFrame = Frame(self.frame, width=300, height=550, bg = "white")
        
    def ShowCallFrame(self, alarm):
                
        self.callFrame.place(x = 0, y = 0)
        self.callFrame.tkraise()
        