from tkinter import Button

class BtnOk:
    
    alarmFrame = None    
    frame = None
    menu = None
    list = None
    btnOk = None
    
    def __init__(self, alarmFrame, frame, menu, list):
        
        self.alarmFrame = alarmFrame
        self.frame = frame
        self.menu = menu
        self.list = list
        self.CreateButton()
        
    def CreateButton(self):
        
        self.btnOk = Button(self.frame, text = "OK", bg = "white", command=self.CloseFrame)
        self.btnOk.place(x = 110, y = 500, height=40, width=80)
        
    def CloseFrame(self):
        
        self.alarmFrame.tkraise()
        self.menu.tkraise()
        self.list.ShowAlarms()