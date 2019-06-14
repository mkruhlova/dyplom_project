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

        master.title("Kartoteka kontrahentow")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        self.table = Table(
            self.master,
            ["ID", "Nazwa Kontrahenta", "Adres kontrahenta", "Symbol Kontahenta"],
        )
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_kartoteka_agent()
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

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ""
        for lst in data:
            s += " ".join(lst) + " "
        print(s)
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
        delete_data_agent(row_id)
