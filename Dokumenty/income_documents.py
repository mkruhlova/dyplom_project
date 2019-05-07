import tkinter as tk
from base_frame import BaseFrame

class Income_docs(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Dokumenty przychodowe")
        master.geometry("850x650+300+200")

