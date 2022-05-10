import imp
from tkinter import Label, Button, LabelFrame, PanedWindow, SUNKEN
from tkinter.ttk import LabelFrame
from Components.Alarms.alarms import Alarms
from PIL import ImageTk, Image
from Components.Alarms.switchAlarmBtn import SwitchBtn
from Components.Alarms.EditPage.editPage import EditPage
from functools import partial

class ListOfAlarms:
        
    frame = None
    window = None 
    switchBtn = None   
    btnOn = None
    btnOff = None
    editPage = None
    menuFrame = None
    
    def __init__(self, frame, window, menuFrame):
        
        self.frame = frame
        self.window = window
        self.menuFrame = menuFrame
        self.btnOn = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\on-button.png").resize((50, 50)))
        self.btnOff = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\off-button.png").resize((50, 50)))
        self.switchBtn = SwitchBtn()
        self.editPage = EditPage(self.window, self.menuFrame, self.frame, self)
        self.ShowAlarms()
        
    def ShowAlarms(self):
        
        print("show")
        
        i = 1
        
        for a in Alarms.alarmsList:
            
            print(i)
            print("Hour: {}".format(a.hour))
            print("Minute: {}".format(a.minute))
            print("On: {}".format(a.on))
            print("days: {}".format(a.days))
            
            labelF = PanedWindow(self.frame, bg = a.color)
            labelF.place(x = 0, y = i * 75, width=300, height= 70)
            
            btn = Button(labelF, bg = a.color, borderwidth=0, relief=SUNKEN, activebackground= a.color, command=partial(self.editPage.ShowEditFrame, a))
            btn.place(x = 0,  y = 0, width=210, height=70)
            
            labelHourMinute = Label(labelF, text = "{}:{}".format(a.hour, a.minute), font=("Calibri", 30))
            labelHourMinute.place(x = 5, y = 0, width=100, height=40, anchor="nw")
            
            labelDescription = Label(labelF, text = "{}".format(a.description), font=("Calibri", 10))
            labelDescription.place(x = 5, y = 45)
            
            
            if a.on == True:                
            
                btn = Button(labelF, image = self.btnOn, borderwidth=0, bg = a.color, command=partial(self.ClickBtn, a))
                
            elif a.on == False:
                
                btn = Button(labelF, image = self.btnOff, borderwidth=0, bg = a.color, command=partial(self.ClickBtn, a))
                
            btn.place(x = 220, y = 6)
            i += 1
            
    def ClickBtn(self, alarm):
        
        self.switchBtn.Switch(alarm)
        self.ShowAlarms()