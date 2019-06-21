from tkinter import Frame, Button, Label, messagebox
from tkinter import ttk
from tkinter.constants import *
from tkinter.ttk import Entry

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

        self.master = master
        self.table = None
        self.row_id_input = None

        storage_names = self.get_storage_names()
        print(storage_names)
        Label(self, text="Magazyny").pack()
        self.combo1 = ttk.Combobox(self, values=storage_names)
        self.combo1.pack()

        master.title("Dokumenty Przychodowe")
        master.geometry("850x650+300+200")
        self.init_table()
        self.init_table_btns()

    def init_table(self):
        inf_about_kontrahent = self.get_inf_about_kontrahent()
        comboboxes = {"1": inf_about_kontrahent}
        disabled = [0, 7]

        self.table = Table(
            self.master,
            self._columns,
            disabled_inp_column=disabled,
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

    def init_table_btns(self):
        Label(self, text="Put your id: ").pack(side="left")
        self.row_id_input = Entry(self)
        self.row_id_input.pack(side="left")

        btn = Button(self, text="Usun wiersz", padx=5, pady=5, command=self.delete_row)
        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Dodaj wiersz", padx=5, pady=5, command=self.add_row)
        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Zapisz", padx=5, pady=5, command=self.save)
        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Zaksięguj", padx=5, pady=5, command=self.ksieguj)
        btn.pack(side="left", padx=5, pady=5)

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
        index = get_doc_mag_max_index()
        self.table.append_n_rows(1)
        self.table.cell(last_row_index, 0, index + 1)

    def save(self):
        d = self.clean()
        insert_income_docs(**d)
        insert_income_docs_into_kartoteka(**d)
        self.init_table_data()

    def clean(self):
        data = self.table.get_data()
        first_row = data[-1]
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
        return d

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
