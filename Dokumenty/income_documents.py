from tkinter import Frame, Button, messagebox, Entry, Label, ttk
from tkinter.constants import *

from tkcalendar import DateEntry

from base_frame import BaseFrame
from conect import insert_income_doc, get_income_docs_rw, delete_income_doc, get_storage_names, \
    select_comp_devision_in_income_doc
from table import Table


class IncomeDocs(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = ["Nr Dok", "Jednostka Firmy", "Data Dok", "Data Ksiegowania", "Wartosc", "Ilosc"]

        self.master = master
        self.table = None
        self.row_id_input = None

        company_names = self.get_company_names()
        print(company_names)
        b = Label(self, text="Magazyny")
        b.pack()
        self.combo1 = ttk.Combobox(self, values=company_names)
        self.combo1.pack()

        ttk.Label(self, text='Choose date').pack(padx=10, pady=10)

        cal = DateEntry(self, width=12, background='darkblue', locale='pl',
                        foreground='white', borderwidth=2, year=2019)
        cal.pack(padx=10, pady=10)

        master.title("Dokumenty Rozchodowe")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        inf_about_company = self.get_inf_about_company()
        comboboxes = {'1': inf_about_company}
        self.table = Table(self.master, self._columns, comboboxes=comboboxes)
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_income_docs_rw()
        result = []
        for row in rows:
            result.append(row)
        if result:
            self.table.set_data(result)

        self.row_id_input_label = Label(self, text='Put your id: ')
        self.row_id_input_label.pack(side='left')

        self.row_id_input = Entry(self)
        self.row_id_input.pack(side='left')

        btn = Button(self, text="Delete row", command=self.delete_row)
        btn.pack(side='left')

        btn = Button(self, text="Add row", command=self.add_row)
        btn.pack(side='left')

        btn = Button(self, text="Save", command=self.save)
        btn.pack(side='left')

    @staticmethod
    def get_inf_about_company():
        company_names = []
        rows = select_comp_devision_in_income_doc()
        for row in rows:
            company_names.append(row[0])
        return company_names

    @staticmethod
    def get_company_names():
        company_names = []
        rows = get_storage_names()
        for row in rows:
            company_names.append(row[0])
        return company_names

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ''
        for lst in data:
            s += ' '.join(lst) + ' '
        print(s)
        first_row = data[-1]
        insert_income_doc(nr_dok=first_row[0], jednostka_firmy=first_row[1], data_dok=first_row[2],
                          data_ksiegowania=[3], wartosc=first_row[4], ilosc=first_row[5])

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
        delete_income_doc(row_id)
