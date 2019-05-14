import tkinter as tk
from base_frame import BaseFrame

class WedlugGrupMatInd(BaseFrame, tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Wedlug Grup Materialowych i Indeksow")
        master.geometry("850x650+300+200")