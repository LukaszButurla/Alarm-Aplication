from tkinter import Label

class AlarmInformation:
    
    frame = None
    
    def __init__(self, frame):
        
        self.frame = frame
                
    def ShowInformation(self, alarm):        
               
        hourAndMinute = Label(self.frame, text = "{}:{}".format(alarm.hour, alarm.minute), font=("Calibri", 50), bg = "white")
        hourAndMinute.place(x = 55, y = 75, height=80, width=180)