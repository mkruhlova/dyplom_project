import tkinter as tk
from base_frame import BaseFrame
from conect import fetch_closed_docs
from table import Table
from utils import without_index


class PeriodClose(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        self._columns = [
            "Nr Dok",
            "Nazwa",
            "Data Dok",
            "Data Ksiegowania",
            "Ilosc",
            "Cena",
            "Wartosc",
        ]

        self.master = master
        self.table = None

        master.title("Zamkniecie miesiaca")
        master.geometry("850x650+300+200")
        self.init_table()
        self.init_table_data()

    def init_table_data(self):
        rows = fetch_closed_docs()
        result = []
        for row in rows:
            r = without_index(row, 1)
            r = without_index(r, 1)
            result.append(r)
        if result:
            self.table.set_data(result)

    def init_table(self):
        self.table = Table(self.master, self._columns)
        self.table.pack(fill=tk.X, padx=10, pady=10)

