#Author: Judith Sturdevant
#
#Python: Version 3.8.1
#
#Tested on mac os

import tkinter as tk
from tkinter import *

import gui
import functions


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        
        self.master = master
        self.master.minsize(500,300) 
        self.master.maxsize(500,300)
        self.master.columnconfigure(1, weight=1)
        self.master.title("Search Directory")
        self.master.configure(bg="#F0F0F0")

        
        gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()






