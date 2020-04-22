#Author: Judith Sturdevant
#
#Python: Version 3.8.1
#
#Tested on mac os

import tkinter as tk
from tkinter import *
import shutil
import os

import main
import functions


def load_gui(self):

    functions.create_db()

    self.source_path = StringVar()

    self.txt_browse_one = tk.Entry(self.master, textvariable = self.source_path)
    self.txt_browse_one.grid(row=0,column=1,rowspan=1,columnspan=1,padx=(10,15),pady=(50,10),sticky=N+E+W)

    self.btn_move_from = tk.Button(self.master,width=9,height=2,text='Move From',command=lambda: functions.select_source_path(self))
    self.btn_move_from.grid(row=0,column=0,padx=(10,10),pady=(46,10),sticky=W)


    self.destination_path = StringVar()
    
    self.txt_browse_two = tk.Entry(self.master, textvariable = self.destination_path)
    self.txt_browse_two.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(10,15),pady=(50,10),sticky=N+E+W)

    self.btn_move_to = tk.Button(self.master,width=9,height=2,text='Move To',command=lambda: functions.select_destination_path(self))
    self.btn_move_to.grid(row=1,column=0,padx=(10,10),pady=(46,10),sticky=W)

    
    
 
    self.btn_move_files = tk.Button(self.master,width=9,height=2,text='Move',command=lambda: select_files(self))
    self.btn_move_files.grid(row=2,column=0,padx=(10,10),pady=(46,10),sticky=W)



# Utilizes: listdir,path.join(), getmtime(), txt files, shutil move()
    
def select_files(self):
    source_path = self.source_path.get()
    destination_path = self.destination_path.get()
    for file in os.listdir(source_path):
        if file.endswith('txt'): 
            filePath = os.path.join(source_path,file)
            shutil.move(filePath, destination_path)
            fileDestination = os.path.join(destination_path,file)
            last_modified = os.path.getmtime(fileDestination)
            functions.data_entry(file,last_modified)
            print(file,last_modified)


    
    

if __name__ == "__main__":
    pass
