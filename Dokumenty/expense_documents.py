from tkinter import Frame, Button, messagebox, Entry, Label, ttk, Text, IntVar
from tkinter.constants import *

from tkcalendar import DateEntry

from base_frame import BaseFrame
from conect import (
    insert_expense_docs,
    get_expense_docs,
    delete_income_doc,
    get_storage_names,
    select_comp_devision_in_income_doc,
    select_names,
    get_doc_mag_max_index,
    update_expense_docs_in_kart, check_if_name_exist)
from config import date_entry_cnf
from table import Table


class ExpenseDocs(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)


        self._columns = [
            "Nr Dok",
            "Jednostka Firmy",
            "Nazwa",
            "Data Dok",
            "Data Ksiegowania",
            "Cena",
            "Wartosc",
            "Ilosc",
        ]

        self.master = master
        self.table = None
        self. \
            row_id_input = None

        company_names = self.get_company_names()
        print(company_names)
        Label(self, text="Magazyny").pack()
        self.combo1 = ttk.Combobox(self, values=company_names)
        self.combo1.pack()

        master.title("Dokumenty Rozchodowe")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        inf_about_company = self.get_inf_about_company()
        get_names = self.get_inf_names()
        comboboxes = {"1": inf_about_company, "2": get_names}
        disabled = [0]
        self.table = Table(
            self.master,
            self._columns,
            disabled_inp_column=disabled,
            comboboxes=comboboxes,
        )
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_expense_docs()
        result = []
        for row in rows:
            result.append(row[:1] + row[2:])
        if result:
            self.table.set_data(result)

        Label(self, text="Wpisz numer dokumentu: ").pack(side="left")
        self.row_id_input = Entry(self)
        self.row_id_input.pack(side="left")

        btn = Button(self, text="Usun wiersz", command=self.delete_row)

        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Dodaj wiersz", command=self.add_row)
        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Zapisz", command=self.save)
        btn.pack(side="left", padx=5, pady=5)



    @staticmethod
    def get_inf_about_company():
        company_names = []
        rows = select_comp_devision_in_income_doc()
        for row in rows:
            company_names.append(row[0])
        return company_names

    @staticmethod
    def get_inf_names():
        staff_names = []
        rows = select_names()
        for row in rows:
            staff_names.append(row[0])
        return staff_names

    @staticmethod
    def get_company_names():
        company_names = []
        rows = get_storage_names()
        for row in rows:
            company_names.append(row[0])
        return company_names

    def add_row(self):
        last_row_index = self.table._number_of_rows
        index = get_doc_mag_max_index()
        self.table.append_n_rows(1)
        self.table.cell(last_row_index, 0, index + 1)

    def save(self):
        data = self.table.get_data()
        first_row = data[-1]
        d = dict(
            nr_dok=first_row[0],
            jednostka_firmy=first_row[1],
            nazwa=first_row[2],
            data_dok=first_row[3],
            data_ksiegowania=first_row[4],
            wartosc=first_row[5],
            ilosc=first_row[6],
            cena=first_row[7],
        )
        if self.is_name_valide(d['nazwa']):
            insert_expense_docs(**d)
            update_expense_docs_in_kart(**d)

    def update_expense_docs_in_kart_save(self):
        wartosc = self.table.get_data()
        if int('wartosc') <= 0:
            messagebox.showwarning("chuj")
            return

    def is_name_valide(self, name):
        if not check_if_name_exist(name):
            messagebox.showwarning("Zla nazwa", "Sprobuj ponownie")
            return False
        return True

    def delete_row(self):
        row_id = self.row_id_input.get()
        if len(row_id) == 0 or not row_id.isnumeric():
            messagebox.showwarning("Zle ID", "Sprobuj ponownie")
            return
        table_data = self.table.get_data()
        index = -1
        for i, row in enumerate(table_data):
            if row[0] == row_id:
                index = i
                break
        if index == -1:
            messagebox.showwarning("Zle ID", "Sprobuj ponownie")
            return

        self.table.delete_row(index)
        delete_income_doc(row_id)
