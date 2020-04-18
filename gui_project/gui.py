#Author: Judith Sturdevant
#
#Python: Version 3.8.1
#
#Tested on mac os

from tkinter import *
import tkinter as tk


import main


def load_gui(self):


    # Defines the listbox with a scrollbar and grid layout
    self.txt_browse_one = tk.Entry(self.master,text='')
    self.txt_browse_one.grid(row=2,column=1,rowspan=1,columnspan=1,padx=(10,5),pady=(55,10),sticky=N+E+W)
    

    self.txt_browse_two = tk.Entry(self.master,text='')
    self.txt_browse_two.grid(row=3,column=1,rowspan=1,columnspan=1,padx=(10,5),pady=(15,10),sticky=N+E+W)
    
    
    
    self.btn_browse_one = tk.Button(self.master,width=12,height=2,text='Browse...',command=lambda: function.addToList(self))
    self.btn_browse_one.grid(row=2,column=0,padx=(25,0),pady=(55,10),sticky=W)
    
    self.btn_browse_two = tk.Button(self.master,width=12,height=2,text='Browse...',command=lambda: function.addToList(self))
    self.btn_browse_two.grid(row=3,column=0,padx=(25,0),pady=(10,5),sticky=W)
    
    
    self.btn_check_files = tk.Button(self.master,width=12,height=4,text='Check for files...',command=lambda: function.addToList(self))
    self.btn_check_files.grid(row=4,column=0,padx=(25,7),pady=(10,10),sticky=E)

    
    self.btn_close = tk.Button(self.master,width=12,height=4,text='Close Program',command=lambda: function.addToList(self))
    self.btn_close.grid(row=4,column=1,padx=(0,7),pady=(10,0),sticky=E)




if __name__ == "__main__":
    pass

    
