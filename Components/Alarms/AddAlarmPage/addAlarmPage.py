from tkinter import Frame


class AddAlarmPage:
    
    window = None
    addFrame = None
    
    def __init__(self, window):
        
        self.frame = window
        self.CreateFrame()
        
    def CreateFrame(self):
        
        self.addFrame = Frame(self.window, width=350, height=550)
        # self.addFrame.place(x = 0, y = 0)
        
    def ShowAddFrame(self):
        
        self.addFrame.place(x = 0, y = 0)
        self.addFrame.tkraise()