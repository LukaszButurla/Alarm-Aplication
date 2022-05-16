from tkinter import Label

class AlarmInformation:
    
    frame = None
    
    def __init__(self, frame):
        
        self.frame = frame
                
    def ShowInformation(self, alarm):        
               
        hourAndMinute = Label(self.frame, text = "{}:{}".format(alarm.hour, alarm.minute), font=("Calibri", 50), bg = "white")
        hourAndMinute.place(x = 55, y = 75, height=80, width=180)
        
        callTIme = Label(self.frame, text = "{}:{}".format(alarm.snoozeHour, alarm.snoozeMinute), font=("Calibri", 35), bg = "white")
        callTIme.place(x = 75, y = 160, height=60, width=140)