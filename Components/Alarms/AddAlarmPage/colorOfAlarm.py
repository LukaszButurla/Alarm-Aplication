import Components.Alarms.AddAlarmPage.alarmConfiguration as aC
from tkinter import Button, Frame, Label, SUNKEN
from PIL import Image, ImageTk
from functools import partial


class ColorOfAlarm:
    
    frame = None
    colorFrame = None
    blueBtn = None
    redBtn = None
    pinkBtn = None
    orangeBtn = None
    blueImg = None
    redImg = None
    pinkImg = None
    orangeImg = None
    blueSelectedImg = None
    redSelectedImg = None
    pinkSelectedImg = None
    orangeSelectedImg = None
        
    def __init__(self, frame):
        
        self.blueImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\blue-circle.png").resize((35, 35)))
        self.redImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\red-circle.png").resize((35, 35)))
        self.pinkImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\pink-circle.png").resize((35, 35)))
        self.orangeImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\orange-circle.png").resize((35, 35)))
        self.blueSelectedImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\blue-selected.png").resize((35, 35)))
        self.redSelectedImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\red-selected.png").resize((35, 35)))
        self.pinkSelectedImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\pink-selected.png").resize((35, 35)))
        self.orangeSelectedImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\orange-selected.png").resize((35, 35)))
        
        self.frame = frame
        
        self.CreateFrame()
        
    def CreateFrame(self):
        
        self.colorFrame = Frame(self.frame, bg = "white", width=300, height=100)
        self.colorFrame.place(x = 0,  y = 280)
        
        txt = Label(self.colorFrame, text = "Select color:", font=("Calibri", 18) ,bg = "white")
        txt.place(x = 0, y = 0)
        
        self.blueBtn = Button(self.colorFrame, image = self.blueImg, borderwidth=0, bg = "white", relief=SUNKEN, activebackground= "white", command=partial(self.SelectColor, "blue"))
        self.blueBtn.place(x = 40, y = 50, width=37, height=37)
        
        self.redBtn = Button(self.colorFrame, image = self.redImg, borderwidth=0, bg = "white", relief=SUNKEN, activebackground= "white", command=partial(self.SelectColor, "red"))
        self.redBtn.place(x = 100, y = 50, width=37, height=37)
        
        self.pinkBtn = Button(self.colorFrame, image = self.pinkImg, borderwidth=0, bg = "white", relief=SUNKEN, activebackground= "white", command=partial(self.SelectColor, "pink"))
        self.pinkBtn.place(x = 160, y = 50, width=37, height=37)
        
        self.orangeBtn = Button(self.colorFrame, image = self.orangeImg, borderwidth=0, bg = "white", relief=SUNKEN, activebackground= "white", command=partial(self.SelectColor, "orange"))
        self.orangeBtn.place(x = 220, y = 50, width=37, height=37)
        
    def SelectColor(self, color):
        
        aC.color = color
                
        self.EditButtons()
        
    def EditButtons(self):
        
        if aC.color == "blue":
            
            self.blueBtn.configure(image = self.blueSelectedImg)
            self.redBtn.configure(image = self.redImg)
            self.pinkBtn.configure(image = self.pinkImg)
            self.orangeBtn.configure(image = self.orangeImg)
            
        elif aC.color == "red":
            
            self.blueBtn.configure(image = self.blueImg)
            self.redBtn.configure(image = self.redSelectedImg)
            self.pinkBtn.configure(image = self.pinkImg)
            self.orangeBtn.configure(image = self.orangeImg)
            
        elif aC.color == "pink":
            
            self.blueBtn.configure(image = self.blueImg)
            self.redBtn.configure(image = self.redImg)
            self.pinkBtn.configure(image = self.pinkSelectedImg)
            self.orangeBtn.configure(image = self.orangeImg)
            
        elif aC.color == "orange":
            
            self.blueBtn.configure(image = self.blueImg)
            self.redBtn.configure(image = self.redImg)
            self.pinkBtn.configure(image = self.pinkImg)
            self.orangeBtn.configure(image = self.orangeSelectedImg)