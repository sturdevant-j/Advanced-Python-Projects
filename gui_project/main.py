#Author: Judith Sturdevant
#
#Python: Version 3.8.1
#
#Tested on mac os

from tkinter import *
import tkinter as tk


import gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # master frame configuration
        self.master = master
        self.master.minsize(675,250) 
        self.master.maxsize(675,250)
        self.master.columnconfigure(1, weight=1)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        # load in the GUI widgets from module
        gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
