import tkinter as tk
from tkinter.constants import *
from base_frame import BaseFrame
from table import Table

class Income_docs(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.master = master
        self.table = None

        master.title("Dokumenty rozchodowe")
        master.geometry("850x650+300+200")
        self.init_table()


    def init_table(self):
        self.table = Table(self.master, ["ID", "Nazwa", "Data"], column_minwidths=[20, 50, None])
        self.table.pack(fill=X, padx=10, pady=10)

        self.table.set_data([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
        self.table.cell(0, 0, " 01 ")
        self.table.cell(0, 1, "Nazwa przykladowa")
        self.table.cell(0, 2,"02/03/2019")

        self.table.cell(1, 0, "02")
        self.table.cell(1, 1, "Nazwa przykladow 1")
        self.table.cell(1, 2, "03/03/2019")

        self.table.cell(2, 0, "03")
        self.table.cell(2, 1, "Nazwa przykladowa 2")
        self.table.cell(2, 2, "04/03/2019")

        self.table.cell(3, 0, "04")
        self.table.cell(3, 1, "Nazwa przykladowa 3")
        self.table.cell(3, 2, "05/03/2019")