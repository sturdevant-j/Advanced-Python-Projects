#Author: Judith Sturdevant
#
#Python: Version 3.8.1
#
#Tested on mac os

import tkinter as tk
from tkinter import *
import tkinter.filedialog

import main
import gui
import sqlite3



def create_db():
    conn = sqlite3.connect('db_text_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_text_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_file TEXT, \
            col_last_modified TIMESTAMP \
            );")
        conn.commit()
    conn.close()

def data_entry(file,last_modified):
    conn = sqlite3.connect('db_text_files.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_text_files(col_file,col_last_modified) VALUES (?,?)", [file, last_modified])
        conn.commit()
    conn.close()
    
def select_source_path(self):
    self.source_path.set(tk.filedialog.askdirectory())


def select_destination_path(self):
    self.destination_path.set(tk.filedialog.askdirectory())

    




if __name__ == "__main__":
    pass
