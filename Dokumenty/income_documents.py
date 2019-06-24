from tkinter import Frame, messagebox
from tkinter.constants import *

from base_frame import BaseFrame
from conect import (
    delete_doc,
    get_income_docs,
    get_storage_names,
    select_agent,
    insert_income_docs,
    get_doc_mag_max_index,
    insert_income_docs_into_kartoteka,
)
from table import Table
from utils import is_datetime_validate, get_current_datetime


class IncomeDocs(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = [
            "Nr Dok",
            "Kontrahent",
            "Nazwa",
            "Data Dok",
            "Data Ksiegowania",
            "Ilosc",
            "Cena",
            "Wartosc",
        ]
        self._disabled_columns = ["Nr Dok", "Wartosc"]

        self.master = master
        self.table = None
        self.row_id_input = None
        self.new_rows_count = 0

        master.title("Dokumenty Przychodowe")
        master.geometry("850x650+300+200")
        self.init_table()
        self.init_table_btns(True)

    def init_table(self):
        inf_about_kontrahent = self.get_inf_about_kontrahent()
        comboboxes = {"Kontrahent": inf_about_kontrahent}

        self.table = Table(
            self.master,
            self._columns,
            disabled_columns=self._disabled_columns,
            comboboxes=comboboxes,
        )
        self.table.pack(fill=X, padx=10, pady=10)
        self.init_table_data()

    def init_table_data(self):
        rows = get_income_docs()
        result = []
        for row in rows:
            r = row[:2] + row[3:]
            result.append(r)
        if result:
            self.table.set_data(result)

    @staticmethod
    def get_inf_about_kontrahent():
        kontrahents_names = []
        rows = select_agent()
        for row in rows:
            kontrahents_names.append(row[0])
        return kontrahents_names

    @staticmethod
    def get_storage_names():
        storage_names = []
        rows = get_storage_names()
        for row in rows:
            storage_names.append(row[0])
        return storage_names

    def add_row(self):
        last_row_index = self.table.number_of_rows
        index = get_doc_mag_max_index() or 0
        self.table.append_n_rows(1)
        self.table.cell(last_row_index, 0, index + 1 + self.new_rows_count)
        self.new_rows_count += 1

    def save(self):
        cleaned_data = self.clean()
        if cleaned_data is None:
            return
        for d in cleaned_data:
            insert_income_docs(**d)
            insert_income_docs_into_kartoteka(**d)
        self.init_table_data()
        self.new_rows_count = 0

    def clean(self):
        result = []
        if self.new_rows_count < 1:
            return None
        data = self.table.get_data()
        data = data[-self.new_rows_count:]
        for first_row in data:
            d = dict(
                nr_dok=first_row[0],
                kontrahent=first_row[1],
                nazwa=first_row[2],
                data_dok=first_row[3],
                data_ksiegowania=first_row[4],
                ilosc=first_row[5],
                cena=first_row[6],
            )
            if not is_datetime_validate(d["data_dok"]):
                messagebox.showwarning("Zle wpisywana data", "Sporobuj ponownie")
                return

            d["wartosc"] = int(d["ilosc"]) * float(d["cena"])
            result.append(d)
        return result

    def delete_row(self):
        row_id = self.row_id_input.get()
        if len(row_id) == 0 or not row_id.isnumeric():
            messagebox.showwarning("Zle podane ID", "Sporobuj ponownie")
            return
        table_data = self.table.get_data()
        index = -1
        for i, row in enumerate(table_data):
            if row[0] == row_id:
                index = i
                break
        if index == -1:
            messagebox.showwarning("Zle podane ID", "Sporobuj ponownie")
            return

        self.table.delete_row(index)
        delete_doc(row_id)

    def ksieguj(self):
        datetime = get_current_datetime()
        last_row_index = self.table.number_of_rows
        self.table.cell(last_row_index - 1, 4, datetime)
