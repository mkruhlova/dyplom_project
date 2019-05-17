from tkinter import Frame
from tkinter.constants import *
from base_frame import BaseFrame
from table import Table


class Expence_docs(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.table = None

        master.title("Dokumenty rozchodowe")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        self.table = Table(self.master, ["column A", "column B", "column C"], column_minwidths=[20, 50, None])
        self.table.pack(fill=X, padx=10, pady=10)

        self.table.set_data([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [10, 11, 12], [10, 11, 12], [10, 11, 12]])
        self.table.cell(0, 0, " a fdas fasd fasdf asdf asdfasdf asdf asdfa sdfas asd sadf ")
        self.table.cell(0, 1, " LOL")
