from tkinter import Frame, Button, Label, Entry, messagebox, ttk
from tkinter.constants import *
from base_frame import BaseFrame
from conect import insert_data_index, select_units, select_materials
from conect import get_kartoteka_index
from conect import delete_data_index
from table import Table


class IndexMat(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = [
            "ID",
            "Nazwa materialu",
            "Jednostka miary",
            "Grupa materialowa",
            "Symbol",
        ]

        self.master = master
        self.table = None
        self.row_id_input = None

        master.title("Indeksy Materialowe")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        units = self.get_units()
        materials = self.get_group_materials()
        comboboxes = {"2": units, "3": materials}
        self.table = Table(self.master, self._columns, comboboxes=comboboxes)
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_kartoteka_index()
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
    def get_group_materials():
        available_materials = []
        rows = select_materials()
        for row in rows:
            available_materials.append(row[0])
        return available_materials

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
        insert_data_index(
            id=first_row[0],
            nazwa_materialu=first_row[1],
            jednostka_miary=first_row[2],
            grupa_materialowa=first_row[3],
            symbol=first_row[4],
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
        delete_data_index(row_id)
