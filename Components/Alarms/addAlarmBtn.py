from Components.Alarms.AddAlarmPage.addAlarmPage import AddAlarmPage
from PIL import Image, ImageTk
from tkinter import Button


class AddAlarmBtn:
    
    window = None
    frame = None
    addBtn = None
    addImg = None
    addAlarmPage = None
    
    def __init__(self, frame, window):
        
        self.window = window
        self.frame = frame
        self.addImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\plus.png").resize((20, 20)))
        self.addAlarmPage = AddAlarmPage(self.window)
        self.CreateAddBtn()
        
        
    def CreateAddBtn(self):
        
        self.addBtn = Button(self.frame, image = self.addImg, borderwidth= 0, bg = "white", command= self.OpenAddPage)
        self.addBtn.place(x = 250, y = 20)
        
    def OpenAddPage(self):
        

        self.addAlarmPage.ShowAddFrame()