from tkinter import Button

class Menu:

    window = None

    def __init__(self, root):
        
        self.window = root
        self.CreateMenu()

    def CreateMenu(self):

        btnClock = Button(self.window)
        btnClock.place(x = 0, y = 490, height=60, width=60)

        btnAlarm = Button(self.window)
        btnAlarm.place(x = 60, y = 490, height=60, width=60)

        btnTimer = Button(self.window)
        btnTimer.place(x = 120, y = 490, height=60, width=60)

        btnTime = Button(self.window)
        btnTime.place(x = 180, y = 490, height=60, width=60)

        btnInfo = Button(self.window)
        btnInfo.place(x = 240, y = 490, height=60, width=60)