from tkinter import Tk, ttk
from Components.Menu.menu import Menu


class Main:

    window = None
    menu = None

    def __init__(self):

        self.ConfigureWindow()
        menu = Menu(self.window)
        self.window.mainloop()

    def ConfigureWindow(self):

        self.window = Tk()
        self.window.geometry("300x550")
        self.window.configure(bg = "white")

        

if __name__ == "__main__":

    Main()
