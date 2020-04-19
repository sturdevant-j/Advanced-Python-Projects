#Author: Judith Sturdevant
#
#Python: Version 3.8.1
#
#Tested on mac os

import tkinter as tk
from tkinter import *

import main
import function


def load_gui(self):

    self.selectedPath = StringVar()

    self.txt_browse_one = tk.Entry(self.master, textvariable = self.selectedPath)
    self.txt_browse_one.grid(row=0,column=1,rowspan=1,columnspan=1,padx=(10,15),pady=(50,10),sticky=N+E+W)
    

    self.btn_check_files = tk.Button(self.master,width=7,height=2,text='Directory',command=lambda: function.select_path(self))
    self.btn_check_files.grid(row=0,column=0,padx=(10,10),pady=(46,10),sticky=W)


    


if __name__ == "__main__":
    pass
