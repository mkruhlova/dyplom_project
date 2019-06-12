from tkinter import Frame, Button, Label, Entry, messagebox
from tkinter.constants import *

from base_frame import BaseFrame
from table import Table
from conect import insert_data_storage, get_storage
from conect import select_symbols_for_storage
from conect import delete_data_storage


class Storage(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        self._columns = ["ID", "Symbol magazynu", "Nazwa magazynu", "Data otwarcia",
                         "Status inwentaryzacji", "Data inwentaryzacji",
                         "Symbol placowki",
                         "ID Dokumentu"]
        self.master = master
        self.table = None
        self.row_id_input = None

        master.title("Magazyny")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        units = self.get_units()
        comboboxes = {'6': units}
        self.table = Table(self.master, self._columns, comboboxes=comboboxes)
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_storage()
        results = []
        for row in rows:
            results.append(row)
        if results:
            self.table.set_data(results)

        self.init_btns()

    @staticmethod
    def get_units():
        available_units = []
        rows = select_symbols_for_storage()
        for row in rows:
            available_units.append(row[0])
        return available_units

    def init_btns(self):
        row_id_input_label = Label(self, text='Put your id: ')
        row_id_input_label.pack(side='left')

        self.row_id_input = Entry(self)
        self.row_id_input.pack(side='left')

        btn = Button(self, text="Delete row", command=self.delete_row)
        btn.pack(side='left')

        btn = Button(self, text="Add row", command=self.add_row)
        btn.pack(side='left')

        btn = Button(self, text="Save", command=self.save)
        btn.pack(side='left')

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ''
        for lst in data:
            s += ' '.join(lst) + ' '
        print(s)
        first_row = data[-1]
        insert_data_storage(id=first_row[0], symbol_magazynu=first_row[1], nazwa_magazynu=first_row[2],
                            data_otwarcia=first_row[3],
                            status_inwentaryzacji=first_row[4],
                            data_inwentaryzacji=first_row[5],
                            symbol_placowki=first_row[6], id_dokumentu=first_row[7])

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
        delete_data_storage(row_id)
