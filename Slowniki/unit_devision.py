from tkinter import Frame, Button
from tkinter.constants import *
from base_frame import BaseFrame
from table import Table
from conect import insert_data_unit
from conect import get_kartoteka_unit
from conect import delete_data


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
        rows = get_kartoteka_unit()
        result = []
        for row in rows:
            result.append(row)
        self.table.set_data(result)


        btn = Button(self, text="Add row", command=self.add_row)
        btn.pack()

        btn = Button(self, text="Save", command=self.save)
        btn.pack()

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ''
        for lst in data:
            s += ' '.join(lst) + ' '
        print(s)
        first_row = data[-1]
        insert_data_unit(ID=first_row[0], Nazwa_jednostki=first_row[1], Symbol=first_row[2])

    def delete_row(self):
        self.table.pop_n_rows(delete_data)


