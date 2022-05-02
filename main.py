from tkinter import Tk, ttk


class Main:

    window = None

    def __init__(self):

        self.ConfigureWindow()
       
    def ConfigureWindow(self):

        self.window = Tk()
        self.window.geometry("350x550")
        self.window.configure(bg = "white")

        self.window.mainloop()

if __name__ == "__main__":

    Main()
