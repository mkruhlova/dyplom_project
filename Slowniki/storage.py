from tkinter import Frame, Button
from tkinter.constants import *

from base_frame import BaseFrame
from table import Table


class Storage(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.table = None

        master.title("Magazyny")
        # master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth(), master.winfo_screenheight()))
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        self.table = Table(self.master, ["Symbol magazynu", "Nazwa magazynu", "Data otwarcia", "Kierownik magazynu",
                                         "Status Magazynu", "Status inwentaryzacji", "Data inwentaryzacji",
                                         "Symbol placowki",
                                         "ID Dokumentu"], column_minwidths=[None, None, None, None, None, None, None,
                                                                            None, None])
        self.table.pack(fill=X, padx=5, pady=5)

        self.table.set_data([[], [], [], []])

        btn = Button(self, text="Add row", command=self.add_row)
        btn.pack()

        btn = Button(self, text="Save", command=self.save)
        btn.pack()

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        print(data)
