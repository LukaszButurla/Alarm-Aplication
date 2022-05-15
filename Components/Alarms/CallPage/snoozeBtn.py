from tkinter import Button

class SnoozeBtn:
    
    frame = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.CreateButton()
        
    def CreateButton(self):
        
        self.snoozeBtn = Button(self.frame, text = "Snooze", bg = "white")
        self.snoozeBtn.place(x = 110, y = 440, height=40, width=80)
        