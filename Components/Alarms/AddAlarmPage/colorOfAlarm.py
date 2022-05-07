from Components.Alarms.AddAlarmPage.alarmConfiguration import Configuration
from tkinter import Button, Frame, Label, SUNKEN
from PIL import Image, ImageTk


class ColorOfAlarm:
    
    frame = None
    colorFrame = None
    configuration = None
    blueBtn = None
    redBtn = None
    pinkBtn = None
    orangeBtn = None
    blueImg = None
    redImg = None
    pinkImg = None
    orangeImg = None
        
    def __init__(self, frame):
        
        self.blueImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\blue-circle.png").resize((35, 35)))
        self.redImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\red-circle.png").resize((35, 35)))
        self.pinkImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\pink-circle.png").resize((35, 35)))
        self.orangeImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\orange-circle.png").resize((35, 35)))
        
        self.frame = frame
        self.configuration = Configuration()
        self.CreateFrame()
        print("init col")
        
    def CreateFrame(self):
        
        self.colorFrame = Frame(self.frame, bg = "white", width=300, height=100)
        self.colorFrame.place(x = 0,  y = 280)
        
        txt = Label(self.colorFrame, text = "Select color:", font=("Calibri", 18) ,bg = "white")
        txt.place(x = 0, y = 0)
        
        self.blueBtn = Button(self.colorFrame, image = self.blueImg, borderwidth=0, bg = "white", relief=SUNKEN, activebackground= "white")
        self.blueBtn.place(x = 40, y = 50, width=37, height=37)
        
        self.redBtn = Button(self.colorFrame, image = self.redImg, borderwidth=0, bg = "white", relief=SUNKEN, activebackground= "white")
        self.redBtn.place(x = 100, y = 50, width=37, height=37)
        
        self.pinkBtn = Button(self.colorFrame, image = self.pinkImg, borderwidth=0, bg = "white", relief=SUNKEN, activebackground= "white")
        self.pinkBtn.place(x = 160, y = 50, width=37, height=37)
        
        self.orangeBtn = Button(self.colorFrame, image = self.orangeImg, borderwidth=0, bg = "white", relief=SUNKEN, activebackground= "white")
        self.orangeBtn.place(x = 220, y = 50, width=37, height=37)