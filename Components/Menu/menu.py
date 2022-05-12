from Pages.alarmsPage import AlarmsPage
from Pages.clockPage import ClockPage
from Pages.timepiecePage import TimepiecePage
from Pages.infoPage import InfoPage
from Pages.timerPage import TimerPage
from PIL import Image, ImageTk
from Assets.Menu import *

from tkinter import Button, Frame

class Menu:

    window = None
    frame = None
    clockPage = None
    timerPage = None
    alarmsPage = None
    infoPage = None
    timepiecePage = None
    
    alarmImg = None
    clockImg = None
    timepieceImg = None
    timerImg = None
    infoImg = None



    def __init__(self, root):
        
        self.window = root
        
        
        self.alarmImg = ImageTk.PhotoImage(Image.open(r"Assets\Menu\alarm-clock.png").resize((30, 30)))
        self.infoImg = ImageTk.PhotoImage(Image.open(r"Assets\Menu\info.png").resize((30, 30)))
        self.timerImg = ImageTk.PhotoImage(Image.open(r"Assets\Menu\timer.png").resize((35, 35)))
        self.clockImg = ImageTk.PhotoImage(Image.open(r"Assets\Menu\clock.png").resize((30, 30)))
        self.timepieceImg = ImageTk.PhotoImage(Image.open(r"Assets\Menu\timepiece.png").resize((32, 32)))
        
        self.CreateMenu()
        self.ShowMenu()
        
        self.timerPage = TimerPage(self.window)
        self.infoPage = InfoPage(self.window)
        self.timepiecePage = TimepiecePage(self.window)
        self.alarmsPage = AlarmsPage(self.window, self.frame)
        self.clockPage = ClockPage(self.window)
        
    def CreateMenu(self):
        
        self.frame = Frame(self.window, height=60, width=300, bg = "white")
        self.frame.place(x = 0, y = 490)

        btnClock = Button(self.frame, image=self.clockImg, command = self.MenuClock, bg = "white", borderwidth=0)
        btnClock.place(x = 10, y = 10, height=40, width=40)

        btnAlarm = Button(self.frame, image = self.alarmImg, command = self.MenuAlarm, bg = "white", borderwidth=0)
        btnAlarm.place(x = 70, y = 10, height=40, width=40)

        btnTimer = Button(self.frame, image= self.timerImg, command = self.MenuTimer, bg = "white", borderwidth=0)
        btnTimer.place(x = 130, y = 10, height=40, width=40)

        btnTime = Button(self.frame, image = self.timepieceImg, command = self.MenuTimepiece, bg = "white", borderwidth=0)
        btnTime.place(x = 190, y = 10, height=40, width=40)

        btnInfo = Button(self.frame, image= self.infoImg, command = self.MenuInfo, bg = "white", borderwidth=0)
        btnInfo.place(x = 250, y = 10, height=40, width=40)
        
    def ShowMenu(self):
        
        self.frame.tkraise()


    def MenuClock(self):
     
        self.clockPage.ShowClockFrame()
        

    def MenuAlarm(self):
        
        self.alarmsPage.ShowAlarmsPage()
        

    def MenuTimepiece(self):

        self.timepiecePage.ShowTimepieceFrame()

    def MenuTimer(self):

        self.timerPage.ShowTimerFrame()

    def MenuInfo(self):

        self.infoPage.ShowInfoPage()