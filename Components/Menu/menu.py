from Pages.alarmsPage import AlarmsPage
from Pages.clockPage import ClockPage
from Pages.timepiecePage import TimepiecePage
from Pages.infoPage import InfoPage
from Pages.timerPage import TimerPage

from tkinter import Button

class Menu:

    window = None
    clockPage = None
    timerPage = None
    alarmsPage = None
    infoPage = None
    timepiecePage = None



    def __init__(self, root):
        
        self.window = root
        self.timerPage = TimerPage(self.window)
        self.alarmsPage = AlarmsPage(self.window)
        self.infoPage = InfoPage(self.window)
        self.timepiecePage = TimepiecePage(self.window)
        self.clockPage = ClockPage(self.window)
        self.CreateMenu()

    def CreateMenu(self):

        btnClock = Button(self.window, command = self.MenuAlarm)
        btnClock.place(x = 0, y = 490, height=60, width=60)

        btnAlarm = Button(self.window, command = self.MenuClock)
        btnAlarm.place(x = 60, y = 490, height=60, width=60)

        btnTimer = Button(self.window, command = self.MenuTimer)
        btnTimer.place(x = 120, y = 490, height=60, width=60)

        btnTime = Button(self.window, command = self.MenuTimepiece)
        btnTime.place(x = 180, y = 490, height=60, width=60)

        btnInfo = Button(self.window, command = self.MenuInfo)
        btnInfo.place(x = 240, y = 490, height=60, width=60)


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