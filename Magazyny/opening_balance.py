from tkinter import Frame, Button, Label, Entry, messagebox, ttk
from tkinter.constants import *
from base_frame import BaseFrame
from conect import (
    get_bilance_otwarcia,
    insert_data_bilans,
    delete_data_bilans,
    select_opening_balance,
    select_units,
)

from table import Table


class BalanceOpen(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = [
            "Index",
            "Lp",
            "Nazwa",
            "Jednostka miary",
            "Ilosc",
            "Cena",
            "Wartosc",
        ]

        self.master = master
        self.table = None
        self.row_id_input = None

        master.title("Bilans otwarcia")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        units = self.get_units()
        comboboxes_data = {"3": units}
        self.table = Table(
            self.master,
            self._columns,
            comboboxes=comboboxes_data,
            column_minwidths=[None, None, None, None, None, None, None],
        )
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_bilance_otwarcia()
        results = []
        for row in rows:
            results.append(row)
        if results:
            self.table.set_data(results)

        self.init_btns()

    @staticmethod
    def get_units():
        available_units = []
        rows = select_units()
        for row in rows:
            available_units.append(row[0])
        return available_units

    @staticmethod
    def get_data_bilance_otwarcia():
        date_of_bilans = []
        rows = select_opening_balance()
        for row in rows:
            date_of_bilans.append(row[0])
        return date_of_bilans

    def init_btns(self):
        row_id_input_label = Label(self, text="Put your id: ")
        row_id_input_label.pack(side="left")

        self.row_id_input = Entry(self)
        self.row_id_input.pack(side="left")

        btn = Button(self, text="Delete row", command=self.delete_row)
        btn.pack(side="left")

        btn = Button(self, text="Add row", command=self.add_row)
        btn.pack(side="left")

        btn = Button(self, text="Save", command=self.save)
        btn.pack(side="left")

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ""
        for lst in data:
            s += " ".join(lst) + " "
        print(s)
        first_row = data[-1]
        insert_data_bilans(
            index=first_row[0],
            lp=first_row[1],
            nazwa=first_row[2],
            jednostka_miary=first_row[3],
            ilosc=first_row[4],
            cena=first_row[5],
            wartosc=first_row[5],
        )

    def delete_row(self):
        row_id = self.row_id_input.get()
        if len(row_id) == 0 or not row_id.isnumeric():
            messagebox.showwarning("Bad row ID", "Please try again")
            return
        table_data = self.table.get_data()
        index = -1
        for i, row in enumerate(table_data):
            if row[0] == row_id:
                index = i
                break
        if index == -1:
            messagebox.showwarning("Bad row ID", "Please try again")
            return

        self.table.delete_row(index)
        delete_data_bilans(row_id)
