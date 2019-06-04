from tkinter import Frame, Button, ttk, Label
from tkinter.constants import *
from base_frame import BaseFrame
from table import Table


class Expence_docs(BaseFrame, Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.table = None

        # w = Label(self, text="Red", bg="red", fg="white")
        # w.pack(anchor="nw")
        self.combo = ttk.Combobox(master, values=["PZ", "RW"])
        self.combo.pack(padx=32, pady=8, anchor="nw")
        self.label_of_combobox = Label(self, text='Typ dokumenta:')
        self.label_of_combobox.pack(anchor="n")

        self.combo = ttk.Combobox(master, values=["Magazyny"])
        self.combo.pack(padx=32, pady=8, anchor="nw")

        self.combo = ttk.Combobox(master, values=["Data"])
        self.combo.pack(padx=32, pady=8, anchor="nw")

        master.title("Dokumenty PZ/RW")
        master.geometry("850x650+300+200")
        self.init_table()

    def init_table(self):
        self.table = Table(self.master, ["Nr Dok", "Data Dok", "Data Ksiegowania", "Wartosc", "Ilosc"],
                           column_minwidths=[20, 50, 50, 50, 50])
        self.table.pack(fill=X, padx=10, pady=10)

        self.table.set_data([[], [], [], [], [], [], []])

        btn = Button(self, text="Add row", command=self.add_row)
        btn.pack()

        btn = Button(self, text="Save", command=self.save)
        btn.pack()

    def add_row(self):
        self.table.append_n_rows(1)

    def save(self):
        data = self.table.get_data()
        s = ''
        for lst in data:
            s += ' '.join(lst) + ' '
        print(s)
        self.cur.execute(
            "INSERT INTO slownik jednostek firm (ID, Nazwa jednostki, Symbol)  VALUES '1','A Aagrh!','the';")
        print(data)
