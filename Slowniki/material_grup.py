from tkinter import Frame, Button, Entry, Label, messagebox, ttk
from tkinter.constants import *
from base_frame import BaseFrame
from conect import get_group_materials, insert_group_materials, delete_group_materials
from table import Table


class GroupMaterials(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.table = None

        master.title("Grupy materiaowe")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        self.table = Table(self.master, ["ID", "Nazwa Grupy", "Symbol"])
        self.table.pack(fill=X, padx=10, pady=10)
        rows = get_group_materials()
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
        insert_group_materials(
            id=first_row[0], nazwa_grupy=first_row[1], symbol=first_row[2]
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
        delete_group_materials(row_id)