from tkinter import Frame, Button, Label, Entry, messagebox
from tkinter.constants import *

from base_frame import BaseFrame
from conect import delete_data_agent
from conect import insert_data_agent
from conect import get_kartoteka_agent
from table import Table


class KardAg(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.table = None
        self._columns = ["ID", "Nazwa Kontrahenta", "Adres kontrahenta", "Symbol Kontahenta"]

        master.title("Kartoteka kontrahentow")
        master.geometry("850x650+300+200")
        self.init_table()
        self.init_table_btns(deleting_text="Podaj ID: ")

    def init_table(self):
        self.table = Table(
            self.master,
            self._columns,
        )
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_kartoteka_agent()
        result = []
        for row in rows:
            result.append(row)
        if result:
            self.table.set_data(result)


    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        first_row = data[-1]
        insert_data_agent(
            id=first_row[0],
            nazwa_kontrahenta=first_row[1],
            adres_kontrahenta=first_row[2],
            symbol_kontrahenta=first_row[3],
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
        delete_data_agent(row_id)
