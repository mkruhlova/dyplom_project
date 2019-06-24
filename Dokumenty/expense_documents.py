from tkinter import Frame, messagebox
from tkinter.constants import *

from base_frame import BaseFrame
from conect import (
    get_expense_docs,
    delete_income_doc,
    get_storage_names,
    select_comp_devision_in_income_doc,
    select_names,
    get_doc_mag_max_index,
    check_if_name_exist,
    insert_expence_docs_into_kartoteka, insert_expence_docs, update_expense_docs_in_kart, insert_expense_docs)
from table import Table
from utils import get_current_datetime, is_datetime_validate


class ExpenseDocs(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = [
            "Nr Dok",
            "Jednostka Firmy",
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
        self.new_rows_count = 0

        master.title("Dokumenty Rozchodowe")
        master.geometry("850x650+300+200")
        self.init_table()
        self.init_table_btns(True)

    def init_table(self):
        inf_about_company = self.get_inf_about_company()
        get_names = self.get_inf_names()
        comboboxes = {"Jednostka Firmy": inf_about_company, "Nazwa": get_names}

        self.table = Table(
            self.master,
            self._columns,
            disabled_columns=self._disabled_columns,
            comboboxes=comboboxes,
        )
        self.table.pack(fill=X, padx=10, pady=10)
        self.init_table_data()

    def init_table_data(self):
        rows = get_expense_docs()
        result = []
        for row in rows:
            r = row[:1] + row[2:]
            result.append(r)
            if result:
                self.table.set_data(result)

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
            if self.is_name_valide(d["nazwa"]):
                val = update_expense_docs_in_kart(**d)
                if val:
                    messagebox.showwarning("Zle dane", "1")
                    return
                insert_expense_docs(**d)
        self.init_table_data()
        self.new_rows_count = 0

    def clean(self):
        """Returns None if data is invalid"""
        result = []
        if self.new_rows_count < 1:
            # Any rows didn't added
            return None
        data = self.table.get_data()
        data = data[-self.new_rows_count:]
        for first_row in data:
            d = dict(
                nr_dok=first_row[0],
                jednostka_firmy=first_row[1],
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

    def ksieguj(self):
        datetime = get_current_datetime()
        last_row_index = self.table.number_of_rows
        try:
            self.table.cell(last_row_index - 1, 4, datetime)
        except IndexError as e:
            print(e)
            messagebox.showwarning("Nie ma co ksiegowac", "Sprobuj ponownie")
