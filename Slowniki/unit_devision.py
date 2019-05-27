from tkinter import Frame, Button
from tkinter.constants import *
from base_frame import BaseFrame
from table import Table


class UnitDev(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.table = None

        master.title("Jednostki miary")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        self.table = Table(self.master, ["ID", "Nazwa jednostki", "Symbol jednostki"], column_minwidths=[20, 50, None])
        self.table.pack(fill=X, padx=10, pady=10)

        self.table.set_data([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

        btn = Button(self, text="Add row", command=self.add_row)
        btn.pack()

        btn = Button(self, text="Save", command=self.save)
        btn.pack()

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        print(data)


