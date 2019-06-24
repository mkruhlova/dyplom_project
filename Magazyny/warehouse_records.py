from tkinter import Frame, messagebox
from tkinter.constants import *

from base_frame import BaseFrame
from conect import (
    delete_income_doc,
    get_kartoteka_unit_for_storage,
    get_storage_records,
    select_warehouse_records,
    insert_warehouse_records,
    select_materials,
)
from table import Table


class WarehouseRec(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = ["Index", "Nazwa", "Ilosc", "Cena", "Wartosc"]

        self.master = master
        self.table = None
        self.row_id_input = None

        master.title("Kartoteki magazynowe")
        master.geometry("850x650+300+200")
        self.init_table()
        self.init_table_btns(deleting_text="Podaj ID: ")

    def init_table(self):
        self.table = Table(self.master, self._columns)
        self.table.pack(fill=X, padx=10, pady=10)
        result = self.get_warehouse_records()
        if result:
            self.table.set_data(result)

    def get_warehouse_records(self):
        result = []
        rows = select_warehouse_records()
        for row in rows:
            result.append(row[:5])
        return result

    @staticmethod
    def get_unit_devision():
        unit_dev_names = []
        rows = get_kartoteka_unit_for_storage()
        for row in rows:
            unit_dev_names.append(row[0])
        return unit_dev_names

    @staticmethod
    def get_group_materials():
        available_materials = []
        rows = select_materials()
        for row in rows:
            available_materials.append(row[0])
        return available_materials

    @staticmethod
    def get_storage_records():
        storage_record = []
        rows = get_storage_records()
        for row in rows:
            storage_record.append(row[0])
        return storage_record

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ""
        for lst in data:
            s += " ".join(lst) + " "
        print(s)
        first_row = data[-1]
        insert_warehouse_records(
            Index=first_row[0],
            Nazwa=first_row[1],
            Jednostka_miary=first_row[2],
            Ilosc=first_row[3],
            Cena=first_row[4],
            Wartosc=first_row[5],
        )

    def delete_row(self):
        row_id = self.row_id_input.get()
        if len(row_id) == 0 or not row_id.isnumeric():
            messagebox.showwarning("Zle podane ID", "Sprobuj ponownie")
            return
        table_data = self.table.get_data()
        index = -1
        for i, row in enumerate(table_data):
            if row[0] == row_id:
                index = i
                break
        if index == -1:
            messagebox.showwarning("Zle podane ID", "Sprobuj ponownie")
            return

        self.table.delete_row(index)
        delete_income_doc(row_id)
