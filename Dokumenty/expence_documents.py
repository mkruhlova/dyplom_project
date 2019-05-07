import tkinter as tk
from base_frame import BaseFrame


class Expence_docs(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Dokumenty rozchodowe")
        master.geometry("850x650+300+200")
