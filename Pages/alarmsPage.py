from tkinter import Frame, Label, Spinbox
from Components.Alarms.listOfAlarms import ListOfAlarms
from Components.Alarms.addAlarmBtn import AddAlarmBtn

class AlarmsPage:

    window = None
    frame = None
    listOfAlarms = None
    addBtn = None

    def __init__(self, root):

        self.window = root
        self.CreateAlarmsPage()
        self.addBtn = AddAlarmBtn(self.frame, self.window)
        self.listOfAlarms = ListOfAlarms(self.frame)
        
    def CreateAlarmsPage(self):

        self.frame = Frame(self.window, height=490, width=350, bg = "white")
        self.frame.place(x = 0, y = 0)
        
        txt = Label(self.frame, text = "Alarms", font=("Calibri", 25), anchor="nw", bg = "white")
        txt.place(x = 5, y = 5, width=110, height=40)

    def ShowAlarmsPage(self):

        self.frame.tkraise()



