from tkinter import Label



class TimepieceTxt:
    
    timepieceTxt = None
    frame = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.ShowTimepiece()
        
    def ShowTimepiece(self):
        
        self.timepieceTxt = Label(self.frame, text = "23:59:59", bg = "white", font=("Calibri", 30))
        self.timepieceTxt.place(x = 50, y = 225, width=200, height=60)
        
    def EditTxt(self, hour, minute, second):
        
        self.timepieceTxt.configure(text = "{}:{}.{}".format(hour, minute, second))