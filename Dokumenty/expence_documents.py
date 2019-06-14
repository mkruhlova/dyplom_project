from tkinter import Frame, Button, Label, messagebox
from tkinter import ttk
from tkinter.constants import *
from tkinter.ttk import Entry

from tkcalendar import DateEntry

from base_frame import BaseFrame
from conect import (
    delete_doc,
    get_docs_pz,
    get_storage_names,
    select_agent,
    insert_doc_unit,
)
from table import Table


class ExpenceDocs(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = [
            "Nr Dok",
            "Kontrahent",
            "Data Dok",
            "Data Ksiegowania",
            "Wartosc",
            "Ilosc",
        ]

        self.master = master
        self.table = None
        self.row_id_input = None

        storage_names = self.get_storage_names()
        print(storage_names)
        b = Label(self, text="Magazyny")
        b.pack()
        self.combo1 = ttk.Combobox(self, values=storage_names)
        self.combo1.pack()

        ttk.Label(self, text="Choose date").pack(padx=10, pady=10)

        cal = DateEntry(
            self,
            width=12,
            background="darkblue",
            locale="pl",
            foreground="white",
            borderwidth=2,
            year=2019,
        )
        cal.pack(padx=10, pady=10)

        master.title("Dokumenty Przychodowe")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):

        inf_about_kontrahent = self.get_inf_about_kontrahent()
        comboboxes = {"1": inf_about_kontrahent}
        self.table = Table(self.master, self._columns, comboboxes=comboboxes)
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_docs_pz()
        result = []
        for row in rows:
            result.append(row)
        if result:
            self.table.set_data(result)

        self.row_id_input_label = Label(self, text="Put your id: ")
        self.row_id_input_label.pack(side="left")

        self.row_id_input = Entry(self)
        self.row_id_input.pack(side="left")

        btn = Button(self, text="Delete row", command=self.delete_row)
        btn.pack(side="left")

        btn = Button(self, text="Add row", command=self.add_row)
        btn.pack(side="left")

        btn = Button(self, text="Save", command=self.save)
        btn.pack(side="left")

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
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ""
        for lst in data:
            s += " ".join(lst) + " "
        print(s)
        first_row = data[-1]
        insert_doc_unit(
            nr_dok=first_row[0],
            kontrahent=first_row[1],
            data_dok=first_row[2],
            data_ksiegowania=[3],
            wartosc=first_row[4],
            ilosc=first_row[5],
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
        delete_doc(row_id)
