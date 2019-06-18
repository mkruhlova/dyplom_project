from tkinter import Frame, Button, Entry, Label, messagebox, ttk
from tkinter.constants import *
from base_frame import BaseFrame
from table import Table
from conect import insert_data
from conect import get_kartoteka
from conect import delete_data


class CompDev(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.table = None

        master.title("Jednostki firmy")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        self.table = Table(self.master, ["ID", "Nazwa Placowki", "Symbol Placowki"])
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_kartoteka()
        result = []
        for row in rows:
            result.append(row)
        if result:
            self.table.set_data(result)

        self.row_id_input_label = Label(self, text="Put your id: ")
        self.row_id_input_label.pack(side="left")

        self.row_id_input = Entry(self)
        self.row_id_input.pack(side="left")

        btn = Button(self, text="Usun wiersz", padx=5, pady=5, command=self.delete_row)
        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Dodaj wiersz", padx=5, pady=5, command=self.add_row)
        btn.pack(side="left", padx=5, pady=5)

        btn = Button(self, text="Zapisz", padx=5, pady=5, command=self.save)
        btn.pack(side="left", padx=5, pady=5)

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ""
        for lst in data:
            s += " ".join(lst) + " "
        print(s)
        first_row = data[-1]
        insert_data(id=first_row[0], nazwa_jednostki=first_row[1], symbol=first_row[2])

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
        delete_data(row_id)
