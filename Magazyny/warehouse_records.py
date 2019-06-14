from tkinter import Frame, Button, Label, messagebox
from tkinter import ttk
from tkinter.constants import *
from tkinter.ttk import Entry

from tkcalendar import DateEntry

from base_frame import BaseFrame
from conect import delete_income_doc, get_kartoteka_unit_for_storage, get_storage_records, select_warehouse_records, \
    insert_warehouse_records, get_bilance_otwarcia, select_materials
from table import Table


class WarehouseRec(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = ["Index", "Nazwa", "Jednostka miary", "Ilosc", "Cena", "Wartosc", "Grupa materialowa"]

        self.master = master
        self.table = None
        self.row_id_input = None

        ttk.Label(self, text='Choose date').pack(padx=10, pady=10)

        cal = DateEntry(self, width=12, background='darkblue', locale='pl',
                        foreground='white', borderwidth=2, year=2019)
        cal.pack(padx=10, pady=10)

        master.title("Kartoteki magazynowe")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        miara_for_storage = self.get_unit_devision()
        materials = self.get_group_materials()
        comboboxes = {'2': miara_for_storage, '6': materials}
        self.table = Table(self.master, self._columns, comboboxes=comboboxes)
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_bilance_otwarcia()
        results = []
        for row in rows:
            row = list(row)
            row = [row[0]] + row[2:]
            results.append(row)
        if results:
            self.table.set_data(results)

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
        s = ''
        for lst in data:
            s += ' '.join(lst) + ' '
        print(s)
        first_row = data[-1]
        insert_warehouse_records(Index=first_row[0], Nazwa=first_row[1], Jednostka_miary=first_row[2],
                                 Ilosc=first_row[3],
                                 Cena=first_row[4],
                                 Wartosc=first_row[5],
                                 Grupa_materialowa=first_row[6])

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
