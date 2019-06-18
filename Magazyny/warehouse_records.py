from tkinter import Frame, Button, Label, messagebox
from tkinter import ttk
from tkinter.constants import *
from tkinter.ttk import Entry
from typing import List

from tkcalendar import DateEntry

from base_frame import BaseFrame
from conect import (
    delete_income_doc,
    get_kartoteka_unit_for_storage,
    get_storage_records,
    select_warehouse_records,
    insert_warehouse_records,
    get_bilance_otwarcia,
    select_materials,
    get_income_docs,
    get_expense_docs,
)
from config import date_entry_cnf
from table import Table
from utils import without_index


class WarehouseRec(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = ["Index", "Nazwa", "Ilosc", "Cena", "Wartosc"]

        self.master = master
        self.table = None
        self.row_id_input = None

        ttk.Label(self, text="Choose date").pack(padx=10, pady=10)

        cal = DateEntry(self, **date_entry_cnf)
        cal.pack(padx=10, pady=10)

        master.title("Kartoteki magazynowe")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        miara_for_storage = self.get_unit_devision()
        # comboboxes = {"2": miara_for_storage}
        self.table = Table(self.master, self._columns)  # , comboboxes=comboboxes)
        self.table.pack(fill=X, padx=10, pady=10)
        result = self.get_warehouse_records()
        if result:
            self.table.set_data(result)

        Label(self, text="Podaj ID: ").pack(side="left")
        self.row_id_input = Entry(self)
        self.row_id_input.pack(side="left")

        btn = Button(self, text="Usun wiersz", command=self.delete_row)
        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Dodaj wiersz", command=self.add_row)
        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Zapisz", command=self.save)
        btn.pack(side="left", padx=5, pady=5)

    def get_warehouse_records(self):
        result = []
        rows = select_warehouse_records()
        for row in rows:
            result.append(row[:5])
        return result
        #
        # for row in bilance_rows:
        #     qq = list(without_index(row, 1))
        #     qq = list(without_index(qq, 2))
        #     result.append(qq)
        #
        # r = self.merge_income_expense(income_rows, expense_rows)
        # for i in range(len(r)):
        #     r[i] = without_index(r[i], 1)
        #     r[i] = without_index(r[i], 2)
        #     r[i] = without_index(r[i], 2)
        # result.extend(r)
        # a = []
        # for r in result:
        #     index = self.get_index_by_name(a, r[1])
        #     if index == -1:
        #         a.append(r)
        #     else:
        #         a[index][2] += r[2]
        #         a[index][3] += r[3]
        #         a[index][4] += r[4]
        #
        # return a

    # def merge_income_expense(self, income_rows, expense_rows):
    #     merged_incomes = self.merge_rows(
    #         [list(without_index(row, 2)) for row in income_rows]
    #     )
    #     print(merged_incomes)
    #
    #     merged_expense = self.merge_rows(
    #         [list(without_index(row, 1)) for row in expense_rows]
    #     )
    #     print(merged_expense)
    #
    #     # if len(merged_incomes) < len(merged_expense):
    #     #     messagebox.showwarning("Please try again", "More expenses than incomes")
    #     #     return
    #
    #     return self.sub_rows(merged_incomes, merged_expense)
    #
    # def merge_rows(self, rows):
    #     result = []
    #     for r in rows:
    #         index = self.get_index_by_name(result, r[2])
    #         if index == -1:
    #             result.append(r)
    #         else:
    #             result[index][5] += r[5]
    #             result[index][6] += r[6]
    #             result[index][7] += r[7]
    #     return result
    #
    # def sub_rows(self, merged_incomes, merged_expense):
    #     for r in merged_incomes:
    #         index = self.get_index_by_name(merged_expense, r[2])
    #         if index != -1:
    #             r[5] -= merged_expense[index][5]
    #             r[6] -= merged_expense[index][6]
    #             r[7] -= merged_expense[index][7]
    #             # if r[5] < 0 or r[6] < 0:
    #             #     messagebox.showwarning("Please try again", "More expenses than incomes")
    #     return merged_incomes
    #
    # def get_index_by_name(self, result: List, name: str):
    #     for i, r in enumerate(result):
    #         if name in r:
    #             return i
    #     return -1

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
