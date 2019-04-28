import tkinter as tk

class Inventory_store(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Inwentaryzacja")
        master.geometry("850x650+300+200")
        self.init_ui()

    def init_ui(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)