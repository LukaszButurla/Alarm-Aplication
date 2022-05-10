from Pages.alarmsPage import AlarmsPage
from Pages.clockPage import ClockPage
from Pages.timepiecePage import TimepiecePage
from Pages.infoPage import InfoPage
from Pages.timerPage import TimerPage
from PIL import Image, ImageTk

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
        
        
        self.alarmImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\alarm-clock.png").resize((40, 40)))
        self.infoImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\info.png").resize((40, 40)))
        self.timerImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\timer.png").resize((40, 40)))
        self.clockImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\clock.png").resize((40, 40)))
        self.timepieceImg = ImageTk.PhotoImage(Image.open(r"C:\Users\Łukasz\Pictures\Saved Pictures\timepiece.png").resize((55, 55)))
        
        self.CreateMenu()
        self.ShowMenu()
        
        self.timerPage = TimerPage(self.window)
        self.infoPage = InfoPage(self.window)
        self.timepiecePage = TimepiecePage(self.window)
        self.alarmsPage = AlarmsPage(self.window, self.frame)
        self.clockPage = ClockPage(self.window)
        
    def CreateMenu(self):
        
        self.frame = Frame(self.window, height=60, width=300)
        self.frame.place(x = 0, y = 490)

        btnClock = Button(self.frame, image=self.clockImg, command = self.MenuClock, bg = "white", borderwidth=0)
        btnClock.place(x = 0, y = 0, height=60, width=60)

        btnAlarm = Button(self.frame, image = self.alarmImg, command = self.MenuAlarm, bg = "white", borderwidth=0)
        btnAlarm.place(x = 60, y = 0, height=60, width=60)

        btnTimer = Button(self.frame, image= self.timerImg, command = self.MenuTimer, bg = "white", borderwidth=0)
        btnTimer.place(x = 120, y = 0, height=60, width=60)

        btnTime = Button(self.frame, image = self.timepieceImg, command = self.MenuTimepiece, bg = "white", borderwidth=0)
        btnTime.place(x = 180, y = 0, height=60, width=60)

        btnInfo = Button(self.frame, image= self.infoImg, command = self.MenuInfo, bg = "white", borderwidth=0)
        btnInfo.place(x = 240, y = 0, height=60, width=60)
        
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