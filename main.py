from tkinter import Tk, ttk
from Components.Menu.menu import Menu
from time import sleep

class Main:

    window = None
    menu = None

    def __init__(self):

        self.ConfigureWindow()
        self.menu = Menu(self.window)
        self.Update()

    def ConfigureWindow(self):

        self.window = Tk()
        self.window.geometry("300x550")
        self.window.configure(bg = "white")

    def Update(self):

        while True:

            sleep(0.1)
            self.menu.clockPage.clock.LoadTime()
            self.menu.clockPage.clock.ShowTime()
            self.window.update()

        

if __name__ == "__main__":

    Main()
